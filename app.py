from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return ''' 
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        body{
            background-color: aliceblue;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
        }

        h1{
            color: red;
            font-size: 3em;
        }
        p{
            font-size: 1.5em;
            color: black;
        }


    </style>
</head>
<body>

    <h1>¡Bienvenido a Flask en docker!</h1>
    <p>Esto es un aplicacion ejecutandose en docker</p>
    <p>Aplicacion realizada por EMANUEL HUERTAS MEDINA - 2959811 - ADSO</p>

    
</body>
</html>

'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)