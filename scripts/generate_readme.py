"""A generator for project READMEs using parameters defined in the
project's metadata and supplemented with definitions from the extra
definitions JSON.
"""

# Import modules
import os
import sys
import json
from typing import List, Dict, Any, Optional, Tuple, Set
from urllib.parse import quote

# Define classes containing metadata

class DefinitionV1:
    """TODO: Document"""

    def __init__(self, name: str, **kwargs) -> None:
        """The constructor for creating a definition.
        
        Parameters
        ----------
        name : str
            The name of the definition.
        short : str
            The shortened name of the definition.
        link : str
            A link to the definition.
        versions : dict[str, str]
            A list of version numbers to their formal name.
        modifiers : dict[str, str]
            A list of modifiers that have an effect on the definition.
        """

        self.name: str = name
        self.short: Optional[str] = kwargs['short'] if 'short' in kwargs else None
        self.link: Optional[str] = kwargs['link'] if 'link' in kwargs else None
        self.versions: Dict[str, str] = kwargs['versions'] if 'versions' in kwargs else {}
        self.modifiers: Dict[str, str] = kwargs['modifiers'] if 'modifiers' in kwargs else {}

    def print_defn(self, version: Optional[str] = None,
            modifier: Optional[str] = None, add_link: bool = True) -> Tuple[Dict[str, str], str]:
        """Prints the definition and returns a tuple of the associated text
        and any additional metadata needed to properly render.

        Parameters
        ----------
        version : str | None (default None)
            The version of the definition to display.
        modifier : str | None (default None)
            The modifier of the definition to display.
        add_link : bool (default True)
            When `False`, will not add the definition link.
        
        Returns
        -------
        tuple[dict[str, str], str]
            The definition and any additional rendering metadata.
        """

        output: dict[str, str] = {}

        # If version, provide version name
        if version:
            output['version'] = f'{self.versions[version]} ({version})' \
                if version in self.versions else version

        # If modifier, provide modifier name
        if modifier:
            output['modifier'] = f' {self.modifiers[modifier]}' \
                if modifier in self.modifiers else (
                    '' if modifier == '_' else modifier
                )

        output['name'] = f'[{self.short if self.short else self.name}]({self.link})' \
            if add_link and self.link else \
            self.short if self.short else self.name

        return (
            output,
            f'*[{self.short}]: {self.name}' if self.short else ''
        )


class ExtraDefinitionsV1:
    """TODO: Document"""

    def __init__(self, **kwargs) -> None:
        """TODO: Document"""

        self.defns: Dict[str, Dict[str, DefinitionV1]] = {}

        # Remove schema version as it isn't necessary anymore
        if 'schema_version' in kwargs:
            kwargs.pop('schema_version')

        # Loops through top layer
        for group, defined_types in kwargs.items(): # type: str, Dict[str, Dict[str, Any]]           
            defn: Dict[str, DefinitionV1] = {}

            # Loop through each defined type
            for defn_key, defn_info in defined_types.items():

                # Check if type is a simple string
                if isinstance(defn_info, str):
                    defn[defn_key] = DefinitionV1(defn_info)
                # Otherwise, it is an object
                else:
                    defn[defn_key] = DefinitionV1(**defn_info)

            self.defns[group] = defn

    def get_definition(self, key: str, group: Optional[str] = None, **kwargs) -> Tuple[str, str]:
        """TODO: Document"""

        # Check if key is a reference
        if key[0] == '#':
            group: str = 'references'
            key = key[1:]

        # If group is none, just return the key
        if group is None or group not in self.defns:
            return ({'name': key}, '')

        # Otherwise, attempt to resolve the definition
        type_defns: Dict[str, DefinitionV1] = self.defns[group]

        return type_defns[key].print_defn(**kwargs) \
            if key in type_defns else ({'name': key}, '')

class SchemaInfoV1:
    """TODO: Document"""

    @classmethod
    def __gen_badge(cls, key: str, text: str, color: str, alt: Optional[str] = None) -> str:
        """TODO: Document"""
        if alt is None:
            alt: str = text
        return f'![{alt}](https://img.shields.io/badge/{quote(key)}-{quote(text)}-{color})'

    @classmethod
    def init_class_data(cls) -> None:
        """Initializes the class level metadata."""

        # Create the status map for int -> badge link
        cls.__status_map: Dict[int, str] = {
             5: SchemaInfoV1.__gen_badge('Status', 'Exactly Reproducible', 'success'),
             4: SchemaInfoV1.__gen_badge('Status', 'Essentially Reproducible', 'green'),
             3: SchemaInfoV1.__gen_badge('Status', 'Partially Reproducible', 'yellow'),
             2: SchemaInfoV1.__gen_badge('Status', 'Mostly Reproducible', 'orange'),
             1: SchemaInfoV1.__gen_badge('Status', 'Not at All Reproducible', 'red'),
             0: SchemaInfoV1.__gen_badge('Status', 'Cannot Attempt Reproducibility', 'ad7aff'),
            -1: SchemaInfoV1.__gen_badge('Status', 'Not Tested', 'lightgrey'),
        }

    def __init__(self, defns: ExtraDefinitionsV1, **kwargs) -> None:
        """TODO: Document"""

        # Read status and convert to badge str
        self.status: str = SchemaInfoV1.__status_map[kwargs['status'] if 'status' in kwargs else -1]

        # Setup information for footer metadata
        self.footers: Set[str] = set()

        # Get file data
        self.files: List[str] = []
        for file in kwargs['files']: # type: Dict[str, Any]
            if 'license' not in file:
                file['license'] = '_'

            file_name_defn: Tuple[dict[str, str], str] = defns.get_definition(
                file['name'], add_link = False)
            file_license_defn: Tuple[dict[str, str], str] = defns.get_definition(file['license'],
                group = 'license')

            # Add info to footers
            if file_name_defn[1]:
                self.footers.add(file_name_defn[1])
            if file_license_defn[1]:
                self.footers.add(file_license_defn[1])

            file_name_defn: str = file_name_defn[0]["name"]
            file_license_defn: str = file_license_defn[0]["name"]

            file_str: str = f'[{file_name_defn}]({file["link"]})' \
                if 'link' in file else file_name_defn

            # Build text string
            self.files.append(
                f'* {file_str} under {file_license_defn}'
            )


        # Get system information
        self.systems: List[str] = []

        # Fancy name to tuples of version number to tested versions
        system_organizer: Dict[str, Dict[str, str]] = {}
        for suffix_modifier, systems in kwargs['systems'].items(): # type: str, List[str]
            # Get system within suffix_modifier
            for system in systems: # type: str
                system = system.split('-', 3)
                if len(system) == 2:
                    system = [system[0], system[1], '_']

                # Get definitions for the system
                system_defn: tuple[dict[str, str], str] = defns.get_definition(
                    system[0], group = 'systems',
                    version = system[1], modifier = system[2]
                )
                if system_defn[1]:
                    self.footers.add(system_defn[1])
                system_defn: dict[str, str] = system_defn[0]

                # Store definitions in temporary location
                system_name: str = f'{system_defn["name"]}{system_defn["modifier"]}'
                if suffix_modifier != '_':
                    system_name = f'{system_name} ({suffix_modifier})'
                if system_name not in system_organizer:
                    system_organizer[system_name]: Dict[str, str] = {}
                system_organizer[system_name][system[1]]: str = system_defn['version']

        # Sort Keys
        organizer_keys: List[str] = list(system_organizer.keys())
        organizer_keys.sort(key = str.casefold)
        for organizer_key in organizer_keys:
            system_versions: Dict[str, str] = system_organizer[organizer_key]

            # Sort Versions
            organizer_versions: List[str] = list(system_versions.keys())
            organizer_versions.sort(key = str.casefold)
            version_list: List[str] = []
            for organizer_version in organizer_versions:
                version_list.append(system_versions[organizer_version])
            version_list: str = ' | '.join(version_list)

            # Generate system badge
            self.systems.append(
                SchemaInfoV1.__gen_badge(organizer_key, version_list,
                    'informational', alt = f'{organizer_key}: {version_list}')
            )


    def generate_readme(self) -> None:
        """TODO: Document"""
        print('---Status---')
        print(self.status)
        print('---Systems---')
        for system in self.systems:
            print(system)
        print('---Files---')
        for file in self.files:
            print(file)
        print('---Footers---')
        for footer in self.footers:
            print(footer)


# Handle main method

def main() -> int:
    """The entrypoint method for this script.

    Returns
    -------
    int
        The exit code of the script.
    """

    # Initialize class data
    SchemaInfoV1.init_class_data()

    # Load extra definitions
    defns: ExtraDefinitionsV1 = None
    with open(f'{os.path.dirname(__file__)}/extra_definitions.json',
            mode = 'r', encoding = 'UTF-8') as file:
        defns = ExtraDefinitionsV1(**json.load(file))

    extra_metadata: Dict[str, Any] = {}
    ## TODO: Hardcode project_metadata in for now for testing values
    with open('../10-1145_3448139-3448167/project_metadata.json', 'r', encoding='UTF-8') as file:
        project_metadata = json.load(file)

        # Move over extra metadata
        extra_metadata = project_metadata['extra']

        # Add all project files extra data
        extra_files: List[Dict[str, Any]] = []
        for project_file in project_metadata['files']:
            extra_files.append(project_file['extra'])
        extra_metadata['files'] = extra_files

    SchemaInfoV1(defns, **extra_metadata).generate_readme()

if __name__ == '__main__':
    sys.exit(main())
