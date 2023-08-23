# Reproduced Research Projects

This is a repository containing all the projects that have been successfully reproduced across multiple systems. Additional files, patches to original files, and a README containing setup instructions are provided with each project.

## Basic Setup Instructions

All projects use [jammies] to setup the necessary workspace. You can install `jammies` via:

```sh
python3 -m pip install 'jammies'
```

> python3 is replaced with `py` on Windows machines. Additionally, the `python3 -m` prefix is unnecessary if `pip` is properly added to the path.

When navigating to any project folder, you should run the following command to setup the necessary project files:

```sh
jammies patch src
```

From there, you can follow the specific instructions associated with each project using the `src` directory as the working directory.

### Optional Dependencies

Some projects require additional configurations not provided by default within `jammies`. As such, you can add optional dependency packages via:

```sh
python3 -m pip install 'jammies[<optional_dependency>]'
```

Each project will specify if anything other than the default `jammies` is necessary for setup.

> If you want to download all optional dependencies of `jammies`, run:
>```sh
>python3 -m pip install 'jammies[all]'
>```
> This is the recommended method to use.

## Generating READMEs

READMEs can be generated using the [`generate_readme.py`][gen] script. This script is currently written for Python 3.11.2 and uses no external packages.

* `generate_readme.py <start_dir> [--force/-f]`
    * `start_dir`: Specify the top directory to start generating READMEs for.
    * `--force/-f`: When specified, will regenerate any existing READMEs instead of skipping them.

## Extra Schema for Project Metadata

```js
// Within project_metadata.json@extra
{
    // The current version of the schema to deserialize this JSON with
    // Allowed Values: 1 (there is only one schema version)
    "schema_version": 1 

    // A value [-1, 5] representing the reproducibility of the work
    // Allowed Values:
    // 5 No deviations from reported results
	// 4 Within confidence interval deviations or typographical errors
	// 3 Somewhat consistent with some deviations
	// 2 Major deviation with few consistent results
	// 1 No consistent results whatsoever
	// 0 No reproducibility attempt can be made
	//-1 Reproducibility not tested (Default)
    "status": int 

    // A list of systems the project has been tested on
    "systems": {
        // Default system information is specified with '_'
        // Python doesn't like empty strings in its dictionaries
        "_": [
            // Formatted as '<system>-<version>[-<modifier>]'
            "windows-10-native", // Windows 10 Native
            "mac-13", // macOS Ventura
            "debian-11", // Debian bullseye
        ],

        // System has required hardware or underlying modifier
        // Modifier gets appended as suffix to the system
        "GPU":  [
            "debian-11" // Debian bullseye (GPU)
        ]
    },

    // A list of languages the project has been tested on
    "languages": {
        // Language key contains list of tested versions
        "r": [
            "4.2" // R 4.2
        ],
        // Can be multiple lists that are mix and matchable
        // Typically will only be one object
        "python": [
            "3.9", // Python 3.9
            "3.10" // Python 3.10
        ]
    },

    // A list of authors for the associated work
    "authors": [
        // ORCiD if available
        // First and last name will be pulled from URL
        "https://orcid.org/0000-0002-9287-4201", // Aaron Haim
        // Otherwise first and last name can be specified manually
        "John Smith"
    ]

    // A list of tags that can be used to group the data
    "groups": [
        // Tags can be any string
        "2022", // Project was released in 2022
        "full_paper" // Project is a full conference paper
    ]

    // A list of links associated with the project
    "links": {
        // Keys are the links
        "https://doi.org/10.17605/osf.io/74bzs": { // Link to OSF Project
            // Name of link to refer to it by
            "name": "Open Science Framework",

            // Value can be list of strings or objects
            "tags": [
                // Strings specify the tag name in the 'value' part of the object
                // License defaults to ARR (All rights reserved)
                "materials",
                {
                    // Tag for link
                    // Can be any string (e.g., 'data', 'materials', 'paper', etc.)
                    "value": "data", // Link holds data

                    // Associated license key for resource tag
                    // If none specified, defaults to ARR (All rights reserved)
                    "license": "mit" // MIT License
                }
            ],

            // A value [-1, 3] representing the accessibility of the key resource
            // Allowed Values:
            // 3 Public to access and use (Default)
            // 2 Public to view but not use
            // 1 Private but can be requested from authors
            // 0 Cannot obtain access
            //-1 Unconfirmed accessibility
            "accessibility": int
        }
    }
}
```

### Extra Schema for Project Files

```js
// Within project_metadata['files']@extra
{
    // The name of the project file
    // Can be a regular string ('test.csv')
    // Or it can be a reference to something in the extra definitions ('#osf')
    "name": "#osf", // Open Science Framework

    // A link to the project file location
    // Link is optional
    "link": "https://doi.org/10.17605/osf.io/74bzs",

    // License of the project file
    // If a key in extra definitions, will be replaced with available information
    // Default is ARR (All Rights Reserved)
    "license": "mit" // Mit License
}
```

## Extra Definitions Schema

```js
{
    // Always 1
    "schema_version": 1,

    // A key value that can be directly associated with an object in the extra section, each section can define their own format
    // Currently used values are 'systems', 'languages', 'groups', 'license', and 'references
    "systems": {
        // Keys can either map to a value indicating the display name
        "docker": "Docker",

        // ...or they can be an object with additional information
        "mac": {
            // The display name of the key
            "name": "macOS",

            // A shortened version of the display name that is identifiable
            // If specified, will have the display name hidden as a tooltip
            "short": "mac"

            // A link to the resource of the key
            // Links are optional
            "link": "https://www.apple.com/macos/",

            // A list of version keys to their modified values, version number will be surrounding in parentheses
            "versions": {
                "12": "Monterey" // Monterey (12)
            }

            // A list of modifiers to specify as a suffix for the system
            "modifiers": {
                "_": "Native" // Default name is macOS Native
                "brew": "Homebrew" // macOS Homebrew
            }
        }
    }

    // References are generic and not for a specific section so they can only be referenced with a '#' before the key
    // e.g., '#osf', '#github', '#drive'
    "references": {
        // Same as above
    }
}
```

## License

For all files (the "Patches") within this repository (the "Repository") for a given author's (the "Authors") reproduced project (the "Project"), permission is granted to the Authors, free of charge, to deal in the Patches without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or seel copies of the Patches, and to permit persons to whom the Patches are furnished to do so. To non-Authors, the Patches are subject to the same permissions granted on the original Project.

The Patches for the Projects that contain exclusive rights are provided within the Repository under [Title 17, Chapter 1, Section 107(1,3) of the United States Code][usc] towards ongoing research of improving the robustness of reproducibility in research. Patches that are requested for removal by the Authors of the Project will be purged.

The Patches are provided "as is", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the Authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the Patches or the use of other dealings in the Patches.

[jammies]: https://pypi.org/project/jammies/
[git]: https://git-scm.com/

[gen]: ./scripts/generate_readme.py

[usc]: https://www.copyright.gov/title17/92chap1.html#107
