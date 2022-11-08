# Flask 101

1. Estructura básica/setup
```
pip install flask
```
2. Rutas/métodos
   - Siempre poner una función abajito de `@app.route`

3. Returns
   - Pueden ser strings o jsons
   - Importar `jsonify` de flask

4. Requests con body
   - Importar `request` de flask

5. Opciones de `run`
   - Puedes poner `app.run(debug=True)` para poder editar el archivo sin tener que reiniciar el servidor
   - Puedes cambiar el puerto con `app.run(port=5005)`

6. Probar requests
   - Usar postman
   - También hay una extensión de VS Code: [Thunder Client](https://marketplace.visualstudio.com/items?itemName=rangav.vscode-thunder-client)