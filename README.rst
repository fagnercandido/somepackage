Execution
===============
To execute the solution, follow the steps:
    - Create the database
        - This solution use the docker postgres image
            - docker pull postgres
                - wait pull of image
            - docker run --rm --name calls -e POSTGRES_PASSWORD=admin -d -p 5432:5432 -v $HOME/docker/volumes/postgres:/var/lib/postgresql/data postgres
            - psql -h localhost -U postgres -d postgres
                - CREATE ROLE admin LOGIN SUPERUSER PASSWORD 'admin';
                - create database calls;
                - grant all privileges on database calls to admin;
                - \connect calls;
                - create table call (
                        id serial not null constraint call_pk primary key,
                        caller_number varchar not null,
                        callee_number varchar not null,
                        start_call timestamp not null,
                        end_call timestamp not null,
                        type_call varchar not null
                    );
    - Execute the file server.py
        - python3 server.py
    - In module sdk
        - use the file client.py
            - in this file is possible calls all endpoints, just follow the signature methods
            - the returns are in wrappers, always with result status, http code and, if exists, the response content
