# README

## Use

1. Create a Trello Power-up for yourself: https://trello.com/power-ups/admin
2. Add your Power-up's API key to your .env
3. Generate an access token to you Trello account using this link:
   - You have to put in your API key at the end.
   - https://trello.com/1/authorize?expiration=never&name=PersonalExportToken&scope=read&response_type=token&key=YOUR API KEY
4. Add your token to your .env
5. Run the script

## Ipython Notebooks in Git

Remeber to put the following filter into the repo's config:

```
[filter "nbstrip_full"]
        clean = "\"jq\" --indent 1 \
                '(.cells[] | select(has(\"outputs\")) | .outputs) = []  \
                | (.cells[] | select(has(\"execution_count\")) | .execution_count) = null  \
                | .metadata = {\"language_info\": {\"name\": \"python\", \"pygments_lexer\": \"ipython3\"}} \
                | .cells[].metadata = {} \
                '"
        smudge = cat
        required = true
```

And also

```
*.ipynb filter=nbstrip_full
```

into `.gitattributes`.

Install [jq](https://stedolan.github.io/jq/) somewhere into `PATH`, if necessary.
