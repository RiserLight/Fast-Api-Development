# Virtual Environment

1. What is virtual environment and what problem it solves?

Ans:
A virtual environment (often abbreviated as "virtualenv") is a tool in Python that helps to manage project-specific dependencies. It essentially creates an isolated environment for each project, allowing different projects to have their own set of dependencies, which can be different from each other and from the system-wide installed packages.

2. Virtual environment jiss folder me banaya jaayega wo bass uss folfer tak hi simit rahega.

3. Key Aspects of Virtual Environments

   1. **Isolation**: Each virtual environment has its own installation directories and does not share dependencies with other virtual environments or the global Python installation.

   2. **Project-Specific Dependencies**: You can install dependencies specific to a project without affecting other projects or the global Python environment.

   3. **Consistenciness**: Virtual environments help maintain consistent dependencies across different development environments (e.g., development, testing, production), which reduces the "it works on my machine" problem.

4. Problems Solved by Virtual Environments

   1. **Dependency Conflicts**: Different projects may require different versions of the same package. Virtual environments prevent conflicts by isolating dependencies for each project.

   2. **Environment Reproducibility**: By using a virtual environment and a requirements file (like `requirements.txt`), you can easily reproduce the same environment across different machines and development stages.

   3. **Clean Global Environment**: Using virtual environments avoids cluttering the global Python installation with project-specific packages, making it easier to manage and avoid unintended interactions between projects.

   4. **Simplified Deployment**: Virtual environments help create consistent deployment environments, which can be crucial for applications running in production.

   5. **Security**: Isolating dependencies can enhance security by reducing the risk of conflicting or outdated packages affecting different projects.

5. **Creating a Virtual Environment**:

   ```sh
   python3 -m venv myenv
   ```

   This command creates a new directory named `myenv` containing the virtual environment.

6. **Activating a Virtual Environment**:

   - On Unix or MacOS:
     ```sh
     source myenv/bin/activate
     ```
     After this relaunch your terminal

7. **Deactivating a Virtual Environment**:

   ```sh
   deactivate
   ```

8. **Installing Packages in a Virtual Environment**:
   Once the virtual environment is activated, you can install packages using `pip`:

   ```sh
   pip3 install package_name
   ```

9. **Freezing Dependencies**:
   To generate a list of installed packages and their versions, use:

   ```sh
   pip3 freeze > requirements.txt
   ```

10. **Installing Dependencies from a File**:
    To install dependencies listed in a `requirements.txt` file, use:
    ```sh
    pip3 install --no-cache-dir -r requirements.txt
    ```

By using virtual environments, developers can ensure that their projects are more manageable, reproducible, and free from dependency conflicts.

10. package we installed when using virtual environment , the code for all those packages will reside in the lib folder of virtual environment.

# Basics of Fastapi

11. Use gitignore generators to generate gitignore for your project.

12. fastapi dev main.py (start the application)

13. FastApi automaticallay serialise the dictionary to json and sends it to the web browser.

14. HTTP defines a set of request methods to indicate the desired action to be performed for a given resource.

## Different HTTP methods:-

    1. GET
    Requests using GET should only retrieve data. It does not have a request body.

    2. HEAD
    The HEAD method asks for a response identical to a GET request, but without the response body.

    3. POST
    The POST method submits an entity to the specified resource, often causing a change in state or side effects on the server.Has request body

    4. PUT
    The PUT method replaces all current representations of the target resource with the request payload.Has request body

    5. DELETE
    The DELETE method deletes the specified resource. It may or may not have request body.

    6. CONNECT
    The CONNECT method establishes a tunnel to the server identified by the target resource.

    7. OPTIONS
    The OPTIONS method describes the communication options for the target resource.

    8. TRACE
    The TRACE method performs a message loop-back test along the path to the target resource.

    9. PATCH
    The PATCH method applies partial modifications to a resource.Has request body.

15. FastAPI me route ka exact match hota hai naki prefix based match.

16. Get request can be seen in browser directly but not other requests.

17. For fastapi framework , uvicorn and hypercorn are web servers.

18. Why we need schema?
    Ans:
    (a) Its pain to get all the values from the body.
    (b) The client can send whatever data they want.
    (c) The data isn't getting validated.
    (d) We ultimately want client to send data in the format we expect.

19. BaseModel aur pydantic ka use karke humlog schema ko validate karte hain. Settings ka case me humlog BaseSettings use karte hain

20. Yadi koi field ko optional banana hai to uska default value dena jaruri hai.

21. Pydantic model ko dictionry me convert karne ke liye use .dict .

22. In api naming always use the prural.

23. In FastAPI, `default` and `default_factory` are parameters used in the `Body` function to provide default values for request parameters.

- `default`: This parameter is used to set a default value for a field. If the field is not provided in the request body, the default value will be used.

- `default_factory`: This parameter is used when you want to set a default value that is a callable. The callable will be called to generate the default value. This is useful when you want to set a mutable default value, such as a list or a dictionary, because the default value is created anew each time the function is called.

Here's an example of how to use `default` and `default_factory` in FastAPI:

```python
from fastapi import FastAPI, Body
from typing import List, Dict

app = FastAPI()

@app.post("/items/")
async def create_item(
    name: str = Body(default="Default Item"),
    description: str = Body(default=None),
    tags: List[str] = Body(default=[]),
    metadata: Dict[str, str] = Body(default_factory=dict)
):
    return {
        "name": name,
        "description": description,
        "tags": tags,
        "metadata": metadata
    }
```

In this example:

- `name` has a default value of "Default Item". If no value is provided for `name` in the request body, "Default Item" will be used.
- `description` also has a default value of `None`, which means if no value is provided for `description`, it will be `None`.
- `tags` is a list of strings. The default value is an empty list `[]`. If no value is provided for `tags`, an empty list will be used.
- `metadata` is a dictionary of strings. The `default_factory` is `dict`, which means if no value is provided for `metadata`, an empty dictionary will be created.

You can test this endpoint with different request bodies to see how the default values are used:

```bash
# Request without any body
curl -X POST http://localhost:8000/items/
# Returns: {"name":"Default Item","description":null,"tags":[],"metadata":{}}

# Request with a custom name and description
curl -X POST http://localhost:8000/items/ -d '{"name": "Custom Item", "description": "This is a custom item"}'
# Returns: {"name":"Custom Item","description":"This is a custom item","tags":[],"metadata":{}}

# Request with tags and metadata
curl -X POST http://localhost:8000/items/ -d '{"tags": ["tag1", "tag2"], "metadata": {"key": "value"}}'
# Returns: {"name":"Default Item","description":null,"tags":["tag1", "tag2"],"metadata":{"key": "value"}}
```

In each of these requests, the default values are used when the corresponding fields are not provided in the request body.

24. url se aane wala cheez str rahega.

25. In FastAPI, the `Body` function is used to define parameters that should be extracted from the request body. The `Body(...)` syntax is used to indicate that the parameter is required. It's shorthand for `Body(default=..., alias=None)`.

Here's what each part of `Body(...)` means:

- `default=...`: This means that the parameter is required. If the client does not provide a value for this parameter in the request body, FastAPI will raise an error. The `...` is a special singleton value used by Python that indicates that the value is missing.

- `alias=None`: This is the default behavior. It means that the parameter name in the function signature should match the name of the field in the request body. If you want to use a different name in the function signature than in the request body, you can specify an alias with `Body(..., alias="actual_field_name_in_request_body")`.

So, in the context of your code:

```python
@app.post("/create-post")
async def post(payload: Union[Post, None] = Body(..., description="Request body")):
    print(payload)
    return payload
```

The `Body(...)` part means that the `payload` parameter is required and should be extracted from the request body. The `payload` parameter is expected to be either a `Post` object or `None`. If the client does not provide a `payload` in the request body, FastAPI will raise an error.

If you want to make the `payload` parameter optional and handle the case where it is not provided, you should set a default value for it. Here's how you can modify the `post` function to make `payload` optional:

```python
@app.post("/create-post")
async def post(payload: Union[Post, None] = Body(None, description="Request body")):
    print(payload)
    return payload
```

In this modified version, `Body(None)` indicates that the `payload` parameter is optional and defaults to `None` if not provided in the request body.

26. 404 = Not Found

'''
2XX Success Codes
3XX Redirection Codes
4XX Client Error Codes
5XX Server Error Codes
'''

27. Fastapi ke andar @app decoration wale function me async har condition me work karega.

28. When we pass the validation into function definition or function return type , it actually tries to do conversion of the incomming data into the corresponding type. If it is not able to do the conversion then it throws the validation error.

29. Rest api me reponse {
    data:[],
    message:"Success or failure",
    status_code:
    }

30. Status codes provide a clear and standardized way for servers to communicate the outcome of a request to clients (browsers, APIs, etc.).

31. To see what all attributes and functions available in an object we use print(dir(object))

32. When we delete something and pass 204 as status code we should not send any data back otherwise fastapi will throw error

33. __init__.py kisi bhi directory ko package banata hai

34. Kisis bhi folder ke andar yadi koi file import kar raha hai to __init__.py file ko uss folder me zaroor rakhna.

35. Fastapi does exact match on routes in a top down manner.

# Databases :

37. f"""""" ka use karke query likhne par sql injections kiya jaa sakta hai.

38. query string me hi likha jaata hai issliye saare variable string format me hona chahiye.

39. Table me chnage yadi kiya hai to commit karo.

40. SQLAlchemy or any orther orm (object relational mapping) has no way to talk to database. So you will need a sql driver (psycopg2) to talk to database.

41. SQLAlchemy cannot modify the schema of table . For modifying the schema of the tables(migration) we need alembic.

42. unzip x.zip -d /path/to/extract unpacks dictionary x.

# Testing

43. pytest -v

44. Pytest will not print any of the print statements . To do so you need to :
    pytest -v -s. This will run all the tests. If you want to test some specific file then:
    pytest -v -s path of file. If you want to disable warnings then use pytest -v -s --disable-warnings.
    -v means verbose i.e show the output of execution.
    ```python
    pytest -v -s --disable-warnings -x
    ```
    (-x tells pytest to stop after one tets is failed)

45. If we want to run multiple test cases then we should use @pytes.mark.parameterize("var1,var2,res",[(1,2,3),(4,5,9)])
    Here pass the same varibles var1,var2,res to function
    ```python
    @pytest.mark.parameterize("var1,var2,res",[(1,2,3),(4,5,9)])
    def test_func(var1,var2,res):
        assert res==var1+var2
    ```

46. I have folder called testing . Inside this folder , I have two folders code and tests. I want to import a from code in another file in tests fodler. How do I do that in python?

Ans: To import a module from one directory into another in Python, you need to ensure that the Python interpreter can locate the modules. Here's how you can achieve this:

### Project Structure

Assuming your project structure looks like this:

```
testing/
├── code/
│   └── a.py
└── tests/
    └── test_b.py
```

You want to import something from `a.py` (inside the `code` folder) into `test_b.py` (inside the `tests` folder).

### Step-by-Step Solution

1. **Ensure `testing` is a Package**: Create `__init__.py` files to make sure that directories are treated as packages. You may need to add `__init__.py` files if they are not already present:

   ```
   testing/
   ├── code/
   │   ├── __init__.py
   │   └── a.py
   └── tests/
       ├── __init__.py
       └── test_b.py
   ```

2. **Adjust Import Path**: In `test_b.py`, use relative or absolute imports.

### Using Absolute Imports

If `testing` is part of your Python path (i.e., you are running your script from the directory containing `testing` or have added it to `sys.path`), you can use an absolute import.

```python
# testing/tests/test_b.py

from testing.code import a

# Use functions or classes from a
a.some_function()
```

### Using Relative Imports

If `testing/tests/test_b.py` is in the same module hierarchy as `testing/code/a.py`, you can use relative imports.

```python
# testing/tests/test_b.py

from ..code import a

# Use functions or classes from a
a.some_function()
```

### Running the Script

When running `test_b.py`, ensure that the `testing` directory is in your Python path. You can do this by running the script from the parent directory of `testing` or by adjusting `sys.path` within the script.

#### Running from Parent Directory

Navigate to the directory that contains `testing` and run:

```sh
python -m testing.tests.test_b
```

#### Adjusting `sys.path`

Modify `sys.path` in your `test_b.py` to include the `testing` directory:

```python
# testing/tests/test_b.py

import sys
import os

# Add the parent directory of `tests` to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from code import a

# Use functions or classes from a
a.some_function()
```

### Example Content for Files

Here's a simple example of what the contents of `a.py` and `test_b.py` might look like:

**`a.py`**:

```python
# testing/code/a.py

def some_function():
    print("Hello from a.py!")
```

**`test_b.py`**:

```python
# testing/tests/test_b.py

from testing.code import a  # Absolute import
# from ..code import a  # Relative import
# or using sys.path modification as shown above

a.some_function()
```

By following these steps, you can import modules from one directory into another within the same project.

30. Any time you will receive an exception , it will cause to fail the test case.
    mock_func.side_effect=Exception("An exception:")
    with pytest.raises(Exception,match="An exception:"):
    await func1();
    func2();

31. Exceptions should be hamdled as a separate test case.

32. assert statement kabhi bhi True hone par kuch return nahi karta hai aur program ko normally chalne deta hai par false hone par Exception raise karke program ko terminate karta hai.

33. fixtures:
    In the context of software testing, particularly with frameworks like pytest, a **fixture** is a function that provides a fixed baseline environment for tests to run. This baseline can include setting up databases, files, or any state that is required for the tests to execute properly. Fixtures help in making the tests more reliable and easier to write by handling setup and teardown processes.

### Key Concepts of Fixtures

1. **Setup and Teardown**: Fixtures manage the setup before a test runs and the teardown after the test has completed. This ensures that each test runs in a consistent environment and that resources are properly cleaned up afterward.

2. **Reusability**: Fixtures can be reused across multiple tests. This reduces redundancy and makes the test code cleaner and easier to maintain.

3. **Scope**: Fixtures can have different scopes, determining how often the setup and teardown processes are performed. Common scopes include:

   - **Function**: The fixture is set up and torn down once per test function.
   - **Class**: The fixture is set up and torn down once per class of tests.
   - **Module**: The fixture is set up and torn down once per module.
   - **Session**: The fixture is set up and torn down once per session, meaning it lasts for the duration of the testing session.

4. **Parameterized Fixtures**: These allow you to run a single fixture with multiple sets of parameters, useful for testing various inputs.

### Example with pytest

Let's look at an example using pytest, a popular testing framework in Python:

#### Directory Structure

```
testing/
├── code/
│   └── a.py
└── tests/
    ├── __init__.py
    ├── conftest.py
    └── test_b.py
```

#### Content of `a.py`

```python
# testing/code/a.py

def add(x, y):
    return x + y
```

#### Content of `conftest.py`

`conftest.py` is a special configuration file for pytest that allows you to define fixtures that are available to all test files in the directory and its subdirectories.

```python
# testing/tests/conftest.py

import pytest

@pytest.fixture
def example_data():
    return {'x': 1, 'y': 2}
```

#### Content of `test_b.py`

```python
# testing/tests/test_b.py

from code.a import add

def test_add(example_data):
    result = add(example_data['x'], example_data['y'])
    assert result == 3
```

### Explanation

1. **Fixture Definition**:

   - In `conftest.py`, we define a fixture called `example_data` using the `@pytest.fixture` decorator. This fixture returns a dictionary with the keys `x` and `y`.

2. **Using the Fixture**:

   - In `test_b.py`, the test function `test_add` includes a parameter named `example_data`. pytest automatically recognizes this parameter and uses the `example_data` fixture, providing its return value to the test function.

3. **Test Execution**:
   - When `test_add` runs, pytest sets up the `example_data` fixture, passing its return value to the test function. The test function uses this data to perform its assertions.

### Benefits of Using Fixtures

- **Consistency**: Ensures that tests run in a consistent environment.
- **Maintainability**: Reduces duplication and makes it easier to update the setup code in one place.
- **Readability**: Makes test functions shorter and more focused on the actual testing logic.

Fixtures are a powerful feature of pytest and other testing frameworks, providing a structured and efficient way to manage the setup and teardown of test environments.

31. Scope of fixture:
    In pytest, you can define the scope of a fixture to control how often the fixture setup and teardown code is run. The available scopes are:

- **function**: The default scope. The fixture is created for each test function.
- **class**: The fixture is created once per test class.
- **module**: The fixture is created once per module (i.e., per file).
- **session**: The fixture is created once per test session.

Here's how you can define the scope of a fixture:

### Defining a Fixture with Function Scope (default)

```python
import pytest

@pytest.fixture
def function_scope_fixture():
    # Setup code
    yield
    # Teardown code
```

### Defining a Fixture with Class Scope

```python
@pytest.fixture(scope="class")
def class_scope_fixture():
    # Setup code
    yield
    # Teardown code
```

### Defining a Fixture with Module Scope

```python
@pytest.fixture(scope="module")
def module_scope_fixture():
    # Setup code
    yield
    # Teardown code
```

### Defining a Fixture with Session Scope

```python
@pytest.fixture(scope="session")
def session_scope_fixture():
    # Setup code
    yield
    # Teardown code
```

### Example Usage in Tests

Here's an example of using these fixtures in tests:

```python
import pytest

@pytest.fixture(scope="function")
def function_scope_fixture():
    print("Setting up function scope fixture")
    yield
    print("Tearing down function scope fixture")

@pytest.fixture(scope="class")
def class_scope_fixture():
    print("Setting up class scope fixture")
    yield
    print("Tearing down class scope fixture")

@pytest.fixture(scope="module")
def module_scope_fixture():
    print("Setting up module scope fixture")
    yield
    print("Tearing down module scope fixture")

@pytest.fixture(scope="session")
def session_scope_fixture():
    print("Setting up session scope fixture")
    yield
    print("Tearing down session scope fixture")

def test_function_scope(function_scope_fixture):
    print("Running test with function scope fixture")

class TestClassScope:
    def test_class_scope(self, class_scope_fixture):
        print("Running test with class scope fixture")

def test_module_scope(module_scope_fixture):
    print("Running test with module scope fixture")

def test_session_scope(session_scope_fixture):
    print("Running test with session scope fixture")
```

### Running the Tests

To run the tests, simply execute pytest in the terminal:

```sh
pytest
```

### Output Explanation

When you run the tests, you'll see the setup and teardown messages indicating the scope of each fixture. For example, the function scope fixture setup and teardown will be executed for each test function, while the class scope fixture will be set up once per class and used for all test methods in that class.

By controlling the scope of fixtures, you can manage resource allocation and cleanup more effectively, optimizing your test suite's performance and clarity.

31. response object ko json me change karo tab usko access kar paaoge.

32.TestClient is used to test api. It acts as same way as request and we can send any request using it.

33. request.json() will show the request in readable format.

34. MagicMock is synchronous function. A coroutine is an asynchronous function like AsyncMock()

35. An event loop is when we let some stuff that takes a long time do it's thing in the background. And when it's all set, the 'event loop' will 'pick it up'." is the most helpful and intuitive definition of event loop I've heard.

36. Certainly! Let's break down the code and explain how decorators work in this context.

37. **Define a decorator function:**

    ```python
    def add_smiley(func):
        def wrapper():
            return func() + " :)"
        return wrapper
    ```

    Here, `add_smiley` is a decorator function. It takes another function (`func`) as an argument and returns a new function (`wrapper`). Inside `wrapper`, it calls the original function `func` and adds a smiley face to its output.

38. **Decorate the function with multiple decorators:**

    ```python
    @add_smiley
    @make_louder
    def greet():
        return "Hello"
    ```

    The `greet` function is decorated with two decorators: `add_smiley` and `make_louder`. This means that the output of `greet` will be processed first by `add_smiley`, and then by `make_louder`.

39. **Call the decorated function:**

    ```python
    print(greet())  # Output: HELLO!!! :)
    ```

    When `greet()` is called, it goes through the decorators. First, `add_smiley` adds a smiley face to the greeting, and then `make_louder` makes the greeting louder by converting it to uppercase and adding exclamation marks. The final output is "HELLO!!! :)".

In summary, decorators in Python allow us to modify the behavior of functions by wrapping them with additional functionality. Multiple decorators can be applied to a single function, and they are applied in the order they are listed, with the innermost decorator being applied first.

36. When a function has multiple decorators , the innermost decorator is applied first.

37. test\_ se ftest file aur function ka naam suru hona chahiye.

38. In fastapi json is same as dict.

39. Yadi koi chhez kisi par dependent hai to usko same file me hona chahiye ya import kiya hona chahiye.

40. Always write fixture in the last in function definition

41. Database concepts:

42. select \* from db_name.movies;

43. use movies db;
    select title,industry from movies;

44. select \* from movies where industry='bollywood'

45. select count(\*) from movies where industry='bollywood';

46. select distinct industry from movies;

47. select \* from movies where title like '%thor\_%';

48. columns ke liye "" aur values ke liye '' use hota hai.

49. json me "" hi use hota hai naki ''

50. select \* from movies where studio=''

51. use command used to select the database.

52. select \* from movies where title is null;

53. select \* from movies where imdb_rating>=9;

54. select \* from movies where imdb_rating between 6 and 8 . [6,8]

55. select \* from movies where release_year==2019 or release_year=2020 or release_year=2021

56. select \* from movies where release_year in {2019,2020,2021}

57. select \* from movies where imdb_rating is not null;

58. select \* from movies_where imdb_rating is null;

59. select \* from movies where industry='hollywood' order by desc LIMIT 5 offset 0;

60. select min(imdb_rating) as min_rating from movies where industry='bollywood';

61. select max(imdb_rating) as max_rating from movies where industry='bollywood';

62. select studio, count(\*) from movies groupby studio;
    (You have to specify all columns in groupby as in select if that column is noit having aggregate function)

63. select studio,count(studio) as cnt round(avg(imdb_rating),1) as avg_rating from movies
    where studio !='' groupby studio order by average rating desc;

64. From where groupby having orderby

65. select release_year,count(\*) as movies_count from movies groupby release_year having movies_count >2 order by movies count desc;

66. Columns in groupby and having should be in select statement as long as they are not having aggregate functions applied on them.

67. select * ,
    case
    when unit='thousand' then revenue/1000
    when unit='billions' then revenue*100
    else revenue

        end
        as revenue_millions from financials;

68. select m.movie_id ,title,budget,revenue ,currency ,unit from movies m
    innser join financials f on m.movie_id=f.movie_id;

69. Join me saare tables ka column select karne ke liye available hota hai.

70. inner join => only common records.

71. left join => All left table records + common records

72. right join => All right table records + common records

73. Full join :- Union of left and right join

74. If we want to get the union of two tables then number of columns selected by two tables should be same.

75. select m.movie_id ,title ,budget ,revenue ,currency ,unit from movies m left join financials f on m.movie_id=f.movies_id
    UNION
    select m.movie_id ,title ,budget ,revenue ,currency ,unit from movies m right join financials f on m.movie_id=f.movies_id

76. select \* from movies cross join financials;

77. seelct m.movie_id,title,budget ,revenue ,currency ,unit ,
    case
    when unit='thousand' then round((revenue-budget)/1000,1)
    when unit ='billions' then round((revenue-budget)\*1000,1)
    else revenue-budget
    end
    as profit_millions from movies as m
    join financials f
    on m.movie_id=f.movie_id;

78. select a.name,m.title from actors a
    inner join movie_actor ma on
    ma.actor_id=a.actor_id
    join movies m on m.movie_id=ma.movie_id
    groupby m.movie_id;

79. Subquery is executed before the parent query.

80. A subquery can return three types of values :-
    (a) Single value
    (b) list of values
    (c) Tables (When the subquery is returning table then cte (common table expressions) are the best way to write those sub query)

81. with
    cte1 as (select a,b from table1),
    cte2 as (select c,d from table2)
    select b,d from cte1 inner join cte2 on cte1.a=cte2.c

82. Difference between List and list:

    The main differences between using `List`, `Tuple`, etc. from the `typing` module versus directly referring to the built-in Python types `list`, `tuple`, etc. are:

    1. **Type Checking and Annotations**:

    - Using the types from the `typing` module (e.g. `List[int]`, `Tuple[str, int]`) allows you to provide more precise type annotations that can be checked by static type checkers like mypy.
    - The built-in types (`list`, `tuple`, etc.) do not support type parameters, so you cannot easily express the expected types of the elements within the container.

    2. **Python Version Support**:

    - In Python versions prior to 3.9, the built-in container types (`list`, `tuple`, etc.) did not support type parameters. You had to use the types from the `typing` module to achieve this.
    - Starting from Python 3.9, the built-in container types do support type parameters, so you can use `list[int]`, `tuple[str, int]`, etc. directly without needing to import from `typing`.

    3. **Editor Support and Tooling**:

    - Using the types from the `typing` module (e.g. `List[int]`) often provides better editor support, such as better auto-completion and type hints, compared to using the built-in types directly.
    - Static type checkers like mypy are designed to work with the types from the `typing` module, so using those types can lead to better type checking and error reporting.

    In terms of limitations when using `List` from `typing`, the main one is that the `List` type is a generic type, which means it needs to be parameterized with the type of the elements in the list. For example, `List[int]` represents a list of integers, while `List[str]` represents a list of strings.

    Some other potential limitations or considerations when using `List` from `typing`:

    - The `List` type is a generic type, so it cannot be directly instantiated. You need to use the built-in `list` type to create list instances.
    - The `List` type is a subtype of the built-in `list` type, so you can use `list` wherever `List` is expected, but not necessarily the other way around.
    - The `List` type is a bit more verbose to use than the built-in `list` type, especially in simple cases where the element type is obvious.

    In summary, using the types from the `typing` module, such as `List`, `Tuple`, etc., provides more precise type annotations and better tooling support, especially in Python versions prior to 3.9. However, in Python 3.9 and above, you can often use the built-in container types directly with type parameters, which can be more concise in some cases.

83. At runtime, the type variables are erased, meaning that the type information is lost. This is why you cannot directly instantiate a generic type like List[int].

84. from typing import List

# Directly trying to instantiate a generic type

try:
List[int]()
except TypeError:
print("Cannot instantiate a generic type directly")

# Correct way to create a list instance

my_list: List[int] = []
my_list.append(1)
my_list.append(2)
print(my_list)

44. EmailStr for valiadting emaail from pydantic.

45. We never store password directly in database. Insted we store the hash of it. For this purpose we use passlib and bcrypt.

46. tags used to group apis into categories.

47. If we hash a password we cannot get back the password i. ehasing is one way.

48. CORS(Cross Origin Resource Sharing) allows you to make requests from a web browser on one domain to a server on a different domain.

49. By default our API will only allow web browsers running on the same domain as our server to make requests to it.

50. Domain me url aur port dono included hai.

51. RealDIctCursor psycopg2 me use karne se humlog ko results column name ke saath milega.

52. **What is `BaseSettings`?**

`BaseSettings` is a class from the Pydantic library that provides a way to manage settings or configurations for your application. It is similar to `BaseModel` but designed specifically for handling settings and environment variables.

**Key Features of `BaseSettings`**

1. **Environment Variable Support**: `BaseSettings` automatically reads values from environment variables. This makes it easy to configure your application using environment variables.

2. **Type Safety**: Like `BaseModel`, `BaseSettings` uses type hints to ensure that the settings are correctly typed. This helps catch errors at runtime and improves code maintainability.

3. **Customizable**: You can customize the sources of settings using the `customise_sources` method. This allows you to load settings from various sources such as JSON files, environment variables, or even custom sources.

4. **Validation**: `BaseSettings` supports the same validation features as `BaseModel`, including data types and additional validations using `Field()`.

**How `BaseSettings` Differs from `BaseModel`**

1. **Purpose**: `BaseSettings` is designed specifically for managing settings and environment variables, whereas `BaseModel` is a general-purpose model class for creating structured data models.

2. **Default Configuration**: `BaseSettings` includes default configuration settings such as automatically reading environment variables, whereas `BaseModel` does not have such defaults.

3. **Validation**: While both classes support validation, `BaseSettings` is designed to handle settings and environment variables, which often require specific validation rules.

**Example Usage**

Here is an example of how you might use `BaseSettings` to manage settings for your application:

```python
from pydantic import BaseSettings

class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"

settings = Settings()
```

In this example, `Settings` is a class that inherits from `BaseSettings`. It defines several settings with type hints and uses the `Config` class to specify that the settings should be loaded from a `.env` file. The `settings` object is then created, which automatically loads the settings from the environment variables specified in the `.env` file[1][2][3][4].

Citations:
[1] https://docs.pydantic.dev/latest/api/pydantic_settings/
[2] https://docs.pydantic.dev/1.10/usage/settings/
[3] https://docs.pydantic.dev/latest/concepts/pydantic_settings/
[4] https://fastapi.tiangolo.com/ru/advanced/settings/
[5] https://stackoverflow.com/questions/76674272/pydantic-basesettings-cant-find-env-when-running-commands-from-different-places

53. Passlib is used for hashing.

54. The `Config` class in `BaseModel` (and `BaseSettings`) serves several important purposes:

55. **Customizing Behavior**: The `Config` class allows you to customize the behavior of the Pydantic model. This includes options like:

    - `title`: The title for the generated JSON schema.
    - `anystr_strip_whitespace`: Whether to strip leading and trailing whitespace for string and byte types.
    - `extra`: Whether to ignore, allow, or forbid extra attributes during model initialization.
    - `allow_mutation`: Whether the model is faux-immutable (i.e., whether `__setattr__` is allowed).
    - And many other options.

56. **Defining Aliases**: You can use the `fields` and `alias_generator` options in the `Config` class to define aliases for your model fields. This is useful when the field names in your data source don't match the field names in your code.

57. **Inheritance and Overriding**: When you inherit from a Pydantic model, the `Config` class allows you to override or extend the configuration of the parent model. This is particularly useful when you have a base model and want to customize the behavior for specific child models.

58. **Validation and Serialization**: The `Config` class can be used to control how the model is validated and serialized. For example, you can use the `json_schema_mode_override` option to control whether the generated JSON schema is for validation or serialization.

59. **Error Handling**: You can use the `error_msg_templates` option in the `Config` class to override the default error messages generated by Pydantic.

By using the `Config` class, you can make your Pydantic models more flexible, maintainable, and tailored to your specific use case. It allows you to centralize and manage the configuration of your models in a structured way, making it easier to evolve and extend your application over time.

Citations:
[1] https://github.com/pydantic/pydantic/discussions/4871
[2] https://stackoverflow.com/questions/70153150/how-can-i-unpack-a-pydantic-basemodel-to-make-a-from-config-class-method
[3] https://field-idempotency--pydantic-docs.netlify.app/usage/model_config/
[4] https://docs.pydantic.dev/latest/api/config/
[5] https://docs.pydantic.dev/1.10/usage/model_config/

54. Jwt token is not encrypted.

# Authenticaation :

1. There are two ways of handling authentication :-
   (a) Session Based
   (b) JWT Based

2. In session based authentication , the api or database stores info if a user is loggedin or not. This is almost outdated method for authentication.

3. The main advantage of jwt token based authentication is that it is stateless i.e it is not stored in db or api.

4. Complete authentication process:-
   (a) User tries to login using the username and password.
   (b) The password is verified and if is matches then jwt token is send as a response.
   (c) When user tries to use protected apis , then he sends payload along with the jwt token in the request head.
   (d) If the token is verified , then only the api calls will be made.

5. The best way to make a route protected is to use jwt middleware

6. jwt token is not encrypted.

7. Jwt token is divided into three parts :-
   (a) Header
   (b) payload
   (c) signature

8. You should never send any confidential data in payload or header as jwt token is not encrypted.

9. Signature is combination of header + payload + your secret key . This secret key is always known to your server and should never be disclosed. It is generally present in docker compose file.

10. To write variable in postman {{variable_name}}

11. When app is starting , the database should get connected and when the app is closed then the database connection should be closed.

12. PyPika is a Python API for building SQL queries. The motivation behind PyPika is to provide a simple interface for building SQL queries without limiting the flexibility of handwritten SQL.

13. Python-multipart: This library is used to handle multipart/form-data requests. It allows the application to handle file uploads.

14. Asyncpg: This library is used for asynchronous PostgreSQL database operations. It allows the application to interact with PostgreSQL databases asynchronously.
    https://www.youtube.com/watch?v=Ep6XExNOPSc

15. aiohttp: used to make api calls asynchronously  
    https://www.youtube.com/watch?v=nFn4_nA_yk8

16. Python collection modules:
    https://www.youtube.com/playlist?list=PLad_euWnylSduKL_csuqnPKPNeK68scR7


17. Based on the search results, the `psycopg2-binary` package is used for the following purposes:

1. **Quick and Easy Installation**: The `psycopg2-binary` package provides a pre-compiled binary version of the `psycopg2` library. This allows users to quickly install the library without having to meet the build requirements, which can be helpful for development and testing environments.

2. **Compatibility with Various Platforms**: The `psycopg2-binary` package includes pre-compiled binaries for different platforms, such as Windows, macOS, and Linux. This makes it easier to install the library on different operating systems without having to compile the source code.

3. **Avoiding Build Dependencies**: The `psycopg2-binary` package does not require the user to have the necessary build dependencies, such as the PostgreSQL client libraries, installed on their system. This can be particularly useful for users who do not have the ability or expertise to install and configure these dependencies.

4. **Faster Installation**: Installing the `psycopg2-binary` package is generally faster than compiling the `psycopg2` library from source, as the user does not have to go through the build process.

However, the search results also indicate that the `psycopg2-binary` package is not recommended for production use. The main reasons are:

1. **Potential Conflicts with System Libraries**: The `psycopg2-binary` package includes its own versions of certain libraries, such as `libpq` and `libssl`, which may conflict with the system-installed versions of these libraries. This can lead to issues with binary upgradeability and compatibility.

2. **Lack of Customization**: By using the pre-compiled binary, users lose the ability to customize the `psycopg2` library to their specific needs, such as linking against a specific version of the PostgreSQL client library.

3. **Potential Performance Issues**: The pre-compiled binaries may not be optimized for the user's specific hardware and software configuration, which could lead to performance issues.

Therefore, the general recommendation is to use the `psycopg2-binary` package for development and testing purposes, but to use the source distribution of `psycopg2` for production environments to ensure better compatibility, customization, and performance.

Citations:
[1] https://pypi.org/project/psycopg2-binary/
[2] https://www.psycopg.org/docs/install.html
[3] https://stackoverflow.com/questions/59811370/how-to-use-psycopg2-binary-in-python
[4] https://www.geeksforgeeks.org/how-to-install-psycopg2-binary-module-in-python/
[5] https://www.geeksforgeeks.org/introduction-to-psycopg2-module-in-python/