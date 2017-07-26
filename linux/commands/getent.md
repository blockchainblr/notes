### getent

```
$ getent [group|hosts|networks|passwd|protocols|services] [keyword]
```
Get contents from hosts, passwd, groups even if they're in DB/LDAP/other

"getent" allows to get the contents of several databases in their native file format even if they are not actually in /etc. For example, if you are using a LDAP or a DB to authenticate your users, you won't find their info by catting /etc/passwd, but "getent passwd" will concatenate /etc/passwd to the LDAP/DB.

```
$ getent hosts <host>
  - Performs reverse DNS lookup
```
```
$ getent passwd `whoami` | cut -d ":" -f 5
	- Prints out, what the users name, notified in the Gecos field is
```
```
$ getent group <group>
	- see the members of a group
```
```
$ getent passwd | cut -d: -f1 | sort
	- List all usernames in alphabetical order
```
```
$ getent services <<serice>>
	- Query well known ports list. Uses /etc/services file
```
```
$ getent services <port_number>
	- Find which service was used by which port number
```
```
getent hosts google.com | awk '{print $1}'
	- Get just the IP for the hostname
```
