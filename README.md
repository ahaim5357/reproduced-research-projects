# Reproduced Research Projects

This is a repository containing all the projects that have been successfully reproduced across multiple systems. Additional files, patches to original files, and a README containing setup instructions are provided with each project.

## Basic Setup Instructions

All projects use [project_patcher] to setup the necessary workspace. You can install `project_patcher` via:

```sh
python3 -m pip install 'project_patcher'
```

> python3 is replaced with `py` on Windows machines. Additionally, the `python3 -m` prefix is unnecessary if `pip` is properly added to the path.

When navigating to any project folder, you should run the following command to setup the necessary project files:

```sh
project_patcher src
```

> If you are using v0.1.0 of `project_patcher`, the command will be:
>```
>project_patcher init
>```

From there, you can follow the specific instructions associated with each project using the `_src` directory as the working directory.

### Optional Dependencies

Some projects require additional configurations not provided by default within `project_patcher`. As such, you can add optional dependency packages via:

```sh
python3 -m pip install 'project_patcher[<optional_dependency>]'
```

Each project will specify if anything other than the default `project_patcher` is necessary for setup.

> As of 0.2.0, if you want to download all optional dependencies of `project_patcher`, run:
>```sh
>python3 -m pip install 'project_patcher[all]'
>```

## Extra Schema for Project Metadata

```js
// Within project_metadata.json@extra
{
    // Always 1
    "schema_version": 1 

    // A value [-1, 5] representing the reproducibility of the work
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
        // Default system information translated using the 'extra_definitions.json'
        "_": [
            // Formatted as '<system>-<version>[-<modifier>]'
            "windows-10", // Windows 10 Native
            "mac-13", // macOS Ventura
            "debian-11", // Debian Bullseye
        ],

        // System has required hardware or underlying modifier
        "XXX":  [
            "debian-11" // Debian Bullseye (XXX)
        ]
    },

    // A list of languages the project has been tested on
    "languages": {
        // Language key contains list of tested versions
        "r": [
            "4.2" // R 4.2.x
        ]
    },

    // A list of authors for the associated work
    "authors": [
        // ORCiD if available
        "https://orcid.org/xxxx-xxxx-xxxx-xxxx",
        // Otherwise first and last name
        "First Last"
    ]

    // A list of tags that can be used to group the data
    "groups": [
        "xxx" // Can be used to group metadata
    ]

    // A list of links associated with the project
    "links": {
        // Keys are the links

        "https://example.com": {
            // Name of link to refer to it by
            "name": "Example",

            // Value can be string/object or list of strings/object
            "tags": [
                // No license specified means ARR default
                "materials",
                {
                    // Tag for link
                    "value": "data",

                    // Associated license key for resource tag
                    "license": "mit"
                }
            ],

            // A value [-1, 3] representing the accessibility of the key resource
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
    // Or it can be a reference to something in the extra definitions ('#github')
    "name": "#github",

    // License of the project file
    // If a key in extra definitions, will be replaced with available information
    "license": "mit"
}
```

## Extra Definitions Schema

```js
{
    // Always 1
    "schema_version": 1,

    // A key value that can be directly associated with an object in the extra section, each section can define their own format
    "systems": {
        // Keys can either map to a value indicating the display name
        "docker": "Docker",

        // ...or they can be an object with additional information
        "mac": {
            // The display name of the key
            "name": "macOS",

            // A link to the resource of the key (default none)
            "link": "https://example.com",

            // A list of version keys to their modified values, version number will be surrounding in parentheses
            "versions": {
                "12": "Monterey" // Monterey (12)
            }

            // A list of modifiers to specify as a suffix for the system
            "modifiers": {
                "_": "Native" // Default name is macOS Native
                "xxx": "XXX" // macOS XXX
            }
        }
    },
    "languages": {
        // Same as systems section
    },
    "license": {
        "mit": {
            // Name of license
            "name": "MIT License",

            // Short code for identifier (SPDX if available)
            "short": "MIT",

            // Link to license text for reading
            "link": "https://example.com"
        }
    },

    // References are generic and not for a specific section so they can only be referenced with a '#' before the key
    "references": {
        "xxx": {
            // Name of reference
            "name": "XXX",

            // A short code representation of the reference
            "short": "XXX"
        }
    }
}
```

## License

For all files (the "Patches") within this repository (the "Repository") for a given author's (the "Authors") reproduced project (the "Project"), permission is granted to the Authors, free of charge, to deal in the Patches without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or seel copies of the Patches, and to permit persons to whom the Patches are furnished to do so. To non-Authors, the Patches are subject to the same permissions granted on the original Project.

The Patches for the Projects that contain exclusive rights are provided within the Repository under [Title 17, Chapter 1, Section 107(1,3) of the United States Code][usc] towards ongoing research of improving the robustness of reproducibility in research. Patches that are requested for removal by the Authors of the Project will be purged.

The Patches are provided "as is", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the Authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the Patches or the use of other dealings in the Patches.

[project_patcher]: https://pypi.org/project/project-patcher/
[git]: https://git-scm.com/

[usc]: https://www.copyright.gov/title17/92chap1.html#107
