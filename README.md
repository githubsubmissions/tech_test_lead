# Tech Test

![food_security_montioring_system_design.drawio.png](_section_1%2Ffood_security_montioring_system_design.drawio.png)

## General

configurations handled in .env for different environments

- threshold configuration
- parallelization for quicker data ingestion
- configurable fetch days
- lazy loading for optimized
- as codebase grows, it can easily connect to an external storages (dbs)

- tests ensure code works before it's merged through CI/CD
- orm use to allow data storage across multiple persistent storage
- archive DB
- partition DB

- if .env has secrets, it should not be committed

Coding Practices
For easier

- Scalability
- Modularity
- Lazy Loading

Design Pattern Guidelines:
o Gang of Four
o DDD (Domain Driven Design)
 application layer – Dto e.g. UserDto
 domain layer – Do e.g. UserDo
 infrastructure layer <> - e.g. User

o Dependency Injection (DI)
 easier testing
o Inversion of Control (IoC)
o Utilize services for business logic
o Utilize repositories for input/output logic (db, api, file)
o Strategy Pattern
o Pipeline Pattern
• Keep It Simple Stupid (KISS)
• Uncle BOB (Clean code book)
o Code should comment itself

General:  https://refactoring.guru/refactoring

PRs & HOW TO CREATE A BRANCH
• Always pull before you push your code
o If you are trying to merge (pr) into a branch, ensure there are no conflicts between branches (i.e. pull that branch into your
branch and resolve conflicts before pushing)
How to make a pr (use gitflow)s
or
feature/<ticket_id>_<short_ticket_title>
