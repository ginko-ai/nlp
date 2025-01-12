```mermaid
flowchart TD
    SML[Super Mario Land\nQ647249] --> PD[Publication Date:\n21 April 1989]
    SML --> N[Nintendo\nQ8093]
    SML --> PG[Platform Game\nQ82B322]
    SML --> GB[Game Boy\nQ186437]
    SML --> SSG[Side-scrolling video game\nQ228714]

    N -->|PUBLISHER| GB
    N -->|MANUFACTURER| GB

    GB -->|INSTANCE OF| HGC[Handheld Game Console\nQ941818]

    style SML fill:#90EE90
    style N fill:#FFD700
    style PG fill:#FF69B4
    style GB fill:#DEB887
    style SSG fill:#9370DB
    style HGC fill:#A9A9A9
    style PD fill:#FFA500
```
