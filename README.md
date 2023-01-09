# What is GitHub Actions?

Platform to automate developer workflows. The CI/CD is only one of many workflows with we can automate with GitHub Actions. 

# What are those workflows?

Automate management tasks as much as possible

- create bugs
- create pull request
- builds
- merge to master
- update version number
- and more

# How GitHub Actions automate these workflows?  

- Listen to Events - when something happen IN ot TO your repository
    - GitHub events (PR created, Issue created, Contributor joined, ...)
- Trigger Workflows - automatic ACTIONS are executable in response
``` 
Issue created (event) -> Sort (action) -> Label created (action) -> Assign it (action) -> Reproduce (action)
```

# CI/CD with GitHub Actions

```mermaid
flowchart LR
    Commit code --> Test;
    Test --> Build;
    Build --> Push;
    Push --> Deploy;
```

Just another CI/CD tool?
- use same tool instead third-party integration
- integrated into code repository
- setup the pipeline is easy
- tool for developers

# DEMO:
 - Create repository
 - Actions - available workflows for reuse
    - Deployment workflows templates
    - Continues integration workflows
    - Automate every process
- Create workflow