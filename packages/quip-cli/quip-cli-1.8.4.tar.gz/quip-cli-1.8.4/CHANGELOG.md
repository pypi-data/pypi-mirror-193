# Changelog

## [1.8.3] - 2023-02-06
[1.8.3]: https://pypi.org/project/quip-cli/1.8.3/
### Added
- New version options added: Beta, RC
### Fixed
- Stonebranch information removed from sample config

## [1.8.2] - 2022-11-22
[1.8.2]: https://pypi.org/project/quip-cli/1.8.2/
### Fixed
- Jenkins project configuration changed
- SonarQube project name format changed

## [1.8.0] - 2022-11-10
[1.8.0]: https://pypi.org/project/quip-cli/1.8.0/
### Added
- Protected branch support added. Now main branch can be protected.
- Default branch support added. Default branch can be develop branch.
- Git Initialize option added. When new repository is created, it will run git commands to initialize the repository on the project folder.
- Badge support added for gitlab repository. By default it will show the status of the jenkins project
- Folder name standartization
- Project Prefix added for the project folder and repositories
- Checkes for fields.yml file updates before build and push operations
### Fixed
- Error message added for incorrect git configuration
- Automatic template determination for download action fixed
- variablePrefix value updated in template.json

## [1.7.5] - 2022-10-13
[1.7.5]: https://pypi.org/project/quip-cli/1.7.5/
### Fixed
- Repository link in Jenkins project fixed


## [1.7.4] - 2022-10-13
[1.7.4]: https://pypi.org/project/quip-cli/1.7.4/
### Added
- If there is a config file in the project folder, it will be used by default

## [1.7.3] - 2022-10-06
[1.7.3]: https://pypi.org/project/quip-cli/1.7.3/
### Changed
- Default value of use_keyring changed to True
- uip-cli dependency changed to 1.3.0
- quip clean will run new uip clean function
- Template zip file name updated similar to extension zip file name
### Fixed
- quip update will not overwrite all config files just update names on existing templates

## [1.7.2] - 2022-10-06
[1.7.2]: https://pypi.org/project/quip-cli/1.7.2/
### Fixed
- External Setup: Correct gitlab url is used in jenkins job creation

## [1.7.0] - 2022-09-30
[1.7.0]: https://pypi.org/project/quip-cli/1.7.0/
### Added
- Keyring module added to store the password securely
- External system setup added. It can create 
    * GitLab repository
    * Jenkins Job
    * SonarQube Job
    * WebHook from GitLab to Jenkins
- Event Templates for Universal Extension can be viewed and modified from fields.yml

### Fixed
- Template identification logic fixed for the commands that doesn't have template parameter
- Event parsing logic updated for old templates
- Extension name in template.json fixed

## [1.6.4] - 2022-09-23
[1.6.4]: https://pypi.org/project/quip-cli/1.6.4/
### Added
- Now if the project name starts with `ut-` it will automatically set
template option.

## [1.6.3] - 2022-09-23
[1.6.3]: https://pypi.org/project/quip-cli/1.6.3/
### Added
- it will use the name from json file when project name is missing. It
was using the folder name before. With this change you will be
able to download templates with capital letters and having "-"
or "_" in their name.
- It will automatically define if the project is extension or template.
So there is no need to set "-t" parameter for most of the commands.
For new and bootstrap commands it is still needed.

## [1.6.2] - 2022-09-23
[1.6.2]: https://pypi.org/project/quip-cli/1.6.2/
### Added
- Dump fields will also dump template main fields
- `quip fields` command will run update by default
- update-sysid will update all the sysId fields without checking the old value.

## [1.6.0] - 2022-09-14
[1.6.0]: https://pypi.org/project/quip-cli/1.6.0/
### Added
- Version files now support wildcard like "*" and "?"
- Updating version will create backup files with prefix: "." 
- Extension build command will rename the zip file with the same format as the UAC


## [1.5.4] - 2022-09-13
[1.5.4]: https://pypi.org/project/quip-cli/1.5.4/
### Added
- script.yml file will be updated for new templates and update command

## [1.5.3] - 2022-09-09
### Fixed
- ".py" extension added to script file names (template only)
- --rename_script option added to update command

## [1.5.1] - 2022-09-09
### Fixed
- dependencies for yaml fixed

## [1.5.0] - 2022-09-09
### Added
- Version: display and update version feature added. Developers can update the version for minor, major or release 
and it will automatically update all possible versions.

## [1.4.4] - 2022-09-08
### Added
- Clean: Clean command added to delete the dist,build and temp folders

## [1.4.3] - 2022-09-08
### Added
- Fields: Preserve Value option added
- Push: Push/Upload command activated for extensions. This command will execute uip command for pushing.
- Pull: Pull/Download command activated for extensions. This command will execute uip command for pushing.


[1.4.3]: https://pypi.org/project/quip-cli/1.4.3/
[1.4.4]: https://pypi.org/project/quip-cli/1.4.4/
[1.5.0]: https://pypi.org/project/quip-cli/1.5.0/
[1.5.1]: https://pypi.org/project/quip-cli/1.5.1/
[1.5.3]: https://pypi.org/project/quip-cli/1.5.3/
