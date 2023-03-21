"""A generator for project READMEs using parameters defined in the
project's metadata and supplemented with definitions from the extra
definitions JSON.
"""

# Import modules
import os
import re
import sys
import json
from typing import List, Dict, Any, Optional, Tuple, Set
from distutils.version import LooseVersion
from urllib.parse import quote
from urllib import request

# Define classes containing metadata

class DefinitionV1:
    """Defines a basic object with metadata using the
    version 1 schema."""

    # pylint: disable=too-few-public-methods
    # Used as an object for clarity.

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
    """Defines a map of available definitions for an
    object's metadata using the version 1 schema."""

    # pylint: disable=too-few-public-methods
    # Used as an object for clarity.

    def __init__(self, **kwargs) -> None:
        """The constructor for creating the definition map.
        """

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
        """Gets the definition and returns a tuple of the associated text
        and any additional metadata needed to properly render.

        Parameters
        ----------
        key : str
            The key of the definition.
        group : str | None (default None)
            The group to pull the definition from. If `key` starts with
            '#', this will be set to 'references'.
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
    """A metadata object containing the compiled information
    of the extra schema data for a project."""

    # pylint: disable=too-many-instance-attributes
    # Contains what is specified of the schema.

    @classmethod
    def __gen_badge(cls, key: str, text: str, color: str, alt: Optional[str] = None) -> str:
        """Generates a badge / shield link for use in markdown.
        
        Parameters
        ----------
        key : str
            The title of the badge.
        text : str
            The text of the badge.
        color : str
            The color of the badge.
        alt : str (default `text`)
            The alternate text if the badge cannot be displayed.

        Returns
        -------
        str
            The badge image for use in markdown.
        """
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

        # Add basic request header
        cls.__request_headers: Dict[str, str] = {
            'Accept': 'application/json'
        }

        # Add accessibility map
        cls.__accessibility: Dict[int, str] = {
             3: 'Public',
             2: 'Public (View Only)',
             1: 'Can Request From Authors',
             0: 'Private',
            -1: 'Unconfirmed Accessibility'
        }

        # Add italics pattern matcher
        cls.__title_matcher: re.Pattern = re.compile(r'\[([^\[\]]+)\](.+)')

    @classmethod
    def __setup_files(cls, defns: ExtraDefinitionsV1,
            files: List[Dict[str, Any]], footers: Set[str]) -> List[str]:
        """Compiles the 'files' into a format consumable by a README.
        
        Parameters
        ----------
        defns : ExtraDefinitionsV1
            The available definitions for the files.
        files: list of dict[str, any]
            A list of files to be compiled.
        footers: set[str]
            A set of footers to add information that should be
            appended at the end of the README.
        
        Returns
        -------
        list of strs
            The compiled data representing the 'files'.
        """
        output: List[str] = []

        for file in files: # type: Dict[str, Any]
            if 'license' not in file:
                file['license'] = '_'

            file_name_defn: Tuple[dict[str, str], str] = defns.get_definition(
                file['name'], add_link = False)
            file_license_defn: Tuple[dict[str, str], str] = defns.get_definition(file['license'],
                group = 'license')

            # Add info to footers
            if file_name_defn[1]:
                footers.add(file_name_defn[1])
            if file_license_defn[1]:
                footers.add(file_license_defn[1])

            file_name_defn: str = file_name_defn[0]["name"]
            file_license_defn: str = file_license_defn[0]["name"]

            file_str: str = f'[{file_name_defn}]({file["link"]})' \
                if 'link' in file else file_name_defn

            # Build text string
            output.append(
                f'* {file_str} under {file_license_defn}'
            )
        return output

    @classmethod
    def __setup_systems(cls, defns: ExtraDefinitionsV1,
            tested_systems: Dict[str, Any], footers: Set[str]) -> List[str]:
        """Compiles the 'systems' into a format consumable by a README.
        
        Parameters
        ----------
        defns : ExtraDefinitionsV1
            The available definitions for the systems.
        tested_systems: dict[str, any]
            A list of systems to be compiled.
        footers: set[str]
            A set of footers to add information that should be
            appended at the end of the README.
        
        Returns
        -------
        list of strs
            The compiled data representing the 'systems'.
        """
        output: List[str] = []

        # Fancy name to tuples of version number to tested versions
        system_organizer: Dict[str, Dict[str, str]] = {}
        for suffix_modifier, systems in tested_systems.items(): # type: str, List[str]
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
                    footers.add(system_defn[1])
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
            organizer_versions.sort(key = LooseVersion)
            version_list: List[str] = []
            for organizer_version in organizer_versions:
                version_list.append(system_versions[organizer_version])
            version_list: str = ' | '.join(version_list)

            # Generate system badge
            output.append(
                SchemaInfoV1.__gen_badge(organizer_key, version_list,
                    'informational', alt = f'{organizer_key}: {version_list}')
            )
        return output

    @classmethod
    def __setup_languages(cls, defns: ExtraDefinitionsV1,
            languages: Dict[str, List[str]]) -> List[str]:
        """Compiles the 'languages' into a format consumable by a README.
        
        Parameters
        ----------
        defns : ExtraDefinitionsV1
            The available definitions for the languages.
        languages: dict[str, list[str]]
            A list of languages to be compiled.
        footers: set[str]
            A set of footers to add information that should be
            appended at the end of the README.
        
        Returns
        -------
        list of strs
            The compiled data representing the 'languages'.
        """
        output: List[str] = []

        # Sort keys
        language_keys: List[str] = list(languages.keys())
        language_keys.sort(key = str.casefold)
        for language in language_keys: # type: str
            lang_name: str = defns.get_definition(
                language, group = 'languages', add_link = False
            )[0]['name']

            # Sort versions
            versions: list[str] = languages[language]
            versions.sort(key = LooseVersion)
            versions: str = ' | '.join(versions)

            # Output to list
            output.append(
                SchemaInfoV1.__gen_badge(lang_name, versions,
                    'informational', alt = f'{lang_name}: {versions}')
            )

        return output

    @classmethod
    def __setup_authors(cls, authors: List[str]) -> List[str]:
        """Compiles the 'authors' into a format consumable by a README.
        
        Parameters
        ----------
        authors: list[str]
            A list of authors to be compiled.
        
        Returns
        -------
        list of strs
            The compiled data representing the 'authors'.
        """
        output: List[str] = []

        for author in authors: # type: str

            # If author is ORCiD, pull name from there
            if author.startswith('https://orcid.org/'):
                req: request.Request = request.Request(author,
                    headers = SchemaInfoV1.__request_headers)

                author_data: Dict[str, Any] = None
                with request.urlopen(req) as response:
                    author_data = json.load(response)
                author_data = author_data['person']['name']

                author_name: str = \
                    f'{author_data["given-names"]["value"]} {author_data["family-name"]["value"]}'
                output.append(f'[{author_name}]({author})')
            else:
                output.append(author)

        return output

    @classmethod
    def __setup_links(cls, defns: ExtraDefinitionsV1,
        links: Dict[str, Any], footers: Set[str]) -> Tuple[str, List[List[str]]]:
        """Compiles the 'links' into a format consumable by a README.
        
        Parameters
        ----------
        defns : ExtraDefinitionsV1
            The available definitions for the links.
        links: dict[str, any]
            A list of links to be compiled.
        footers: set[str]
            A set of footers to add information that should be
            appended at the end of the README.
        
        Returns
        -------
        tuple[str, list[list[str]]]
            A tuple containing the title of the original project and
            the compiled data representing the 'links'.
        """

        paper: str = ''
        output: List[List[str]] = []

        # Run through links
        for link, metadata in links.items(): # type: str, Dict[str, Any]
            link_data: List[str] = []


            # Get name of resource
            name: Tuple[dict[str, str], str] = defns.get_definition(
                metadata['name'], add_link = False)
            if name[1]:
                footers.add(name[1])
            name = f'[{name[0]["name"]}]({link})'
            accessibility: int = metadata['accessibility'] \
                if 'accessibility' in metadata else 3
            link_data.append(
                f'* {name} ({SchemaInfoV1.__accessibility[accessibility]})'
            )

            # Handle Tags
            for tag in metadata['tags']:
                # Convert string to default object
                if isinstance(tag, str):
                    tag: Dict[str, Any] = {
                        'value': tag,
                        'license': '_'
                    }

                # Treat everything as object now
                tag_license: Tuple[dict[str, str], str] = defns.get_definition(tag['license'],
                    group = 'license')
                if tag_license[1]:
                    footers.add(tag_license[1])
                tag_name: str = tag['value']
                link_data.append(
                    f'    * Contains {tag_name} under {tag_license[0]["name"]}'
                )

                # Get paper name for resource
                if not paper and tag_name == 'paper':
                    paper = name

            output.append(link_data)

        return (paper, output)

    def __init__(self, defns: ExtraDefinitionsV1, **kwargs) -> None:
        """The constructor for compiling the project metadata into a
        human-readable format.
        
        Parameters
        ----------
        defns : ExtraDefinitionsV1
            The available definitions for the files.
        """

        # Read status and convert to badge str
        self.status: str = SchemaInfoV1.__status_map[kwargs['status'] if 'status' in kwargs else -1]
        # Setup information for footer metadata
        self.footers: Set[str] = set()

        # Setup metadata
        self.files: List[str] = SchemaInfoV1.__setup_files(defns, kwargs['files'], self.footers)
        self.systems: List[str] = SchemaInfoV1.__setup_systems(defns, kwargs['systems'],
            self.footers)
        self.languages: List[str] = SchemaInfoV1.__setup_languages(defns, kwargs['languages'])
        self.authors: List[str] = SchemaInfoV1.__setup_authors(kwargs['authors'])
        self.title, self.links = SchemaInfoV1.__setup_links(defns, kwargs['links'], self.footers)

    def generate_readme(self, out_dir: str) -> None:
        """Generates a README file in the specified directory.
        
        Parameters
        ----------
        out_dir : str
            The directory to generate the README to.
        """

        italics_title: re.Match[str] = SchemaInfoV1.__title_matcher.match(self.title)
        italics_title: str = f'[*{italics_title[1]}*]{italics_title[2]}'

        with open(f'{out_dir}/README.md', mode = 'w', encoding = 'UTF-8') as readme:
            print(f'# {self.title}', file = readme)
            print('', file = readme)

            print(self.status, file = readme)
            print('', file = readme)

            print('This is a project constructor ' \
                + ('and patcher ' if os.path.exists(f'{out_dir}/_patches') else '') \
                + f'for the paper {italics_title} by {", ".join(self.authors)}.',
                file = readme)
            print('', file = readme)

            print('### Associated Metadata', file = readme)
            print('', file = readme)

            print('#### Tested Systems', file = readme)
            print('', file = readme)
            for system in self.systems:
                print(f'{system}  ', file = readme)
            print('', file = readme)

            print('#### Languages', file = readme)
            for language in self.languages:
                print(f'{language}  ', file = readme)
            print('', file = readme)

            print('#### Resources', file = readme)
            print('', file = readme)
            for link_group in self.links:
                for link in link_group:
                    print(link, file = readme)
            print('', file = readme)

            print('## Project Files', file = readme)
            print('', file = readme)
            print('The constructor downloads the following files: ', file = readme)
            for file in self.files:
                print(file, file = readme)
            print('', file = readme)

            if os.path.exists(info_path := f'{out_dir}/instructions.md'):
                with open(info_path, mode = 'r', encoding = 'UTF-8') as info:
                    readme.write(info.read())
                print('', file = readme)

            if os.path.exists(info_path := f'{out_dir}/issues.md'):
                with open(info_path, mode = 'r', encoding = 'UTF-8') as info:
                    readme.write(info.read())
                print('', file = readme)

            for footer in self.footers:
                print(footer, file = readme)

def check_and_gen_readme(defns: ExtraDefinitionsV1, start_dir: str, force: bool = False) -> None:
    """Checks to see whether a README should be generated in the current
    directory and generates it if applicable. When a README shouldn't be
    generated, the method checks all subdirectories instead.
    
    Parameters
    ----------
    defns : ExtraDefinitionsV1
        The available definitions for the files.
    start_dir : path-like
        The directory to start recursing through to generate READMEs.
    force : bool (default False)
        When True, regenerates already existing READMEs.
    """

    # Check if project metadata is in current directory
    if os.path.exists(metadata_path := f'{start_dir}/project_metadata.json'):
        if not force and os.path.exists(f'{start_dir}/README.md'):
            print(f'README exists in \'{start_dir}\', skipping!')
            return

        print(f'Generating README for \'{start_dir}\'.')

        # Setup project metadata
        extra_metadata: Dict[str, Any] = {}
        with open(metadata_path, mode = 'r', encoding = 'UTF-8') as file:
            metadata: Dict[str, Any] = json.load(file)

            # Move over extra metadata
            extra_metadata = metadata['extra']

            # Add all project files extra data
            extra_files: List[Dict[str, Any]] = []
            for project_file in metadata['files']:
                extra_files.append(project_file['extra'])
            extra_metadata['files'] = extra_files

        # Generate README
        SchemaInfoV1(defns, **extra_metadata).generate_readme(start_dir)

    # Otherwise, loop through subdirectories and attempt to generate readme for those
    else:
        for entry in os.scandir(start_dir):
            if entry.is_dir():
                check_and_gen_readme(defns, entry.path, force = force)

# Handle main method

def main(start_dir: str = os.curdir, force: bool = False) -> int:
    """The entrypoint method for this script. Generates READMEs
    for all projects within the specified directory.

    Parameters
    ----------
    start_dir : path-like (default '.')
        The directory to start recursing through to generate READMEs.
    force : bool (default False)
        When True, regenerates already existing READMEs.

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

    check_and_gen_readme(defns, start_dir, force = force)

if __name__ == '__main__':
    # Setup parameters
    params: Dict[str, str] = {}
    if len(sys.argv) > 1:
        params['start_dir'] = sys.argv[1]
        if len(sys.argv) > 2:
            for arg in sys.argv[2:]:
                if arg in ['-f', '--force']:
                    params['force'] = True
    
    # Execute main function
    sys.exit(main(**params))
