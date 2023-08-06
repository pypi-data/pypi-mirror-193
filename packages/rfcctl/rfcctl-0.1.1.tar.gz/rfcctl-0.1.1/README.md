# rfcctl: RFC like document manager

&cop; 2023 SiLeader.

## How to use
### 1. Add context
Add context to use `context add` subcommand.

```bash
rfcctl context add --name <CONTEXT_NAME> --user <USER NAME> /path/to/directory
```

- `--name` is context name alias
- `--user` is writer username
- `--switch` option is switch this context as default context
- `--initial-status` is RFC's initial status. default is Draft
- `--obsoleted-status` is obsoleted RFC's status. default is Obsoleted
- `--init` option is create `skeleton.md` in this directory

### 2. Create new RFC
Create new RFC file from `skeleton.md` to use `create` subcommand.

```bash
rfcctl create --category-tree <CATEGORY> <SUBCATEGORY in CATEGORY> ... --title 'My new RFC'
```

### 3. Update RFC metadata
Update RFC's obsoleted metadata to use `update` subcommand.

```bash
rfcctl update
```


## License
Apache License 2.0

See LICENSE