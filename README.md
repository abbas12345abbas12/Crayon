# Crayon 🖍️
### Really tiny ASGI web framework

<img src="https://img.shields.io/github/license/xArty4/Cryon?style=plastic">


# Introduction
#### Crayon is a tool to build simple asynchronous  applications using as few abstractions.

#### It's built on top of uvicorn which is one of the fastest ASGI servers out there  

# Example
```py
import crayon

@crayon.asgi_applications()
async def application(request):
    print(request.text)
    return crayon.Respone('Hello World!')

if __name__ == '__main__':
    from uvicorn.main import run # Using uvicorn to run it or any ASGI server
    run(
        'test:application',
        host='localhost',
        port=5000,
    )
```