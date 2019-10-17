# ericsysmin.python3

Ansible role that installs and sets system or user to use python3 via python

## Requirements

-   Ubuntu >= 16.04
-   Debian >= 9
-   RHEL >= 7
-   CentOS >= 7

## Role Variables

| Variable                  | Required | Default                      | Comments                                                        |
| ------------------------- | -------- | ---------------------------- | --------------------------------------------------------------- |
| `python3_package_name`    | Optional | `python3`                    | Name of the python package                                      |
| `python3_executable_name` | Optional | `{{ python3_package_name }}` | Name of the python executable                                   |
| `python3_default_system`  | Optional | `false`                      | Set /usr/bin/python to /usr/bin/{{ python3_executable_name }}   |
| `python3_default_profile` | Optional | `false`                      | Set 'alias python={{ python3_executable_name}}' in /etc/profile |
| `python3_default_user`    | Optional | `false`                      | Set 'alias python={{ python3_executable_name}}' in ~/.bashrc    |

## Example Playbook

Simply install python3 no changes to `python` executable.

```yaml
- hosts: servers
  roles:
    - role: ericsysmin.python3
```

Configure current user to use python3

```yaml
- hosts: servers
  roles:
    - role: ericsysmin.python3
      python3_default_user: true
```

Configure all users to use python3

```yaml
- hosts: servers
  roles:
    - role: ericsysmin.python3
      python3_default_profile: true
```

Configure system to use python3 **USE WITH CAUTION**

```yaml
- hosts: servers
  roles:
    - role: ericsysmin.python3
      python3_default_system: true
```

## License

MIT

## Author Information

[ericsysmin](https://ericsysmin.com)
