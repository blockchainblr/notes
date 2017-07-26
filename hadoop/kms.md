### KMS ACL Rules
#####Allowing Key Access
In order to perform an operation, <op> on a key <key>, a user
```
1. Must be allowed by <hadoop.kms.acl.OP>
2. Not disallowed by <hadoop.kms.blacklist.OP>
```
and allowed by any of the 3 conditions below
```
3. <whitelist.key.acl.OP>
4. <default.key.acl.OP> if there is no <key.acl.KEY.OP> entry
5. <key.acl.KEY.OP>
```
