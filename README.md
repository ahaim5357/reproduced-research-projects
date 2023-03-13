# Reproduced Research Projects

This is a repository containing all the projects that have been successfully reproduced across multiple systems. Additional files, patches to original files, and a README containing setup instructions are provided with each project.

## Basic Setup Instructions

All projects use [project-patcher] to setup the necessary workspace. You can install `project-patcher` via:

```sh
python3 -m pip install 'project_patcher'
```

> python3 is replaced with `py` on Windows machines. Additionally, the `python3 -m` prefix is unnecessary if `pip` is properly added to the path.

When navigating to any project folder, you should run the following command to setup the necessary project files:

```sh
project_patcher init
```

From there, you can follow the specific instructions associated with each project using the `_src` directory as the working directory.

### Specific Cases

Some projects require additional configurations not provided by default within `project-patcher`. As such, you can add optional dependency packages via:

```sh
python3 -m pip install 'project_patcher[<optional_dependency>]'
```

Each project will specify if anything other than the default `project-patcher` is necessary for setup.

## License

For all files (the "Patches") within this repository (the "Repository") for a given author's (the "Authors") reproduced project (the "Project"), permission is granted to the Authors, free of charge, to deal in the Patches without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or seel copies of the Patches, and to permit persons to whom the Patches are furnished to do so. To non-Authors, the Patches are subject to the same permissions granted on the original Project.

The Patches for the Projects that contain exclusive rights are provided within the Repository under [Title 17, Chapter 1, Section 107(1,3) of the United States Code][usc] towards ongoing research of improving the robustness of reproducibility in research. Patches that are requested for removal by the Authors of the Project will be purged.

The Patches are provided "as is", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the Authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the Patches or the use of other dealings in the Patches.

[project-patcher]: https://pypi.org/project/project-patcher/
[git]: https://git-scm.com/

[usc]: https://www.copyright.gov/title17/92chap1.html#107
