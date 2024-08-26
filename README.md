1. get_dict_value(dct, path)
Propósito: Esta función toma un diccionario dct y una cadena path que representa la ruta para acceder a un valor específico dentro de ese diccionario.
Detalles:
La cadena path se divide en una lista de claves (keys) usando el punto . como delimitador.
Luego, se recorre la lista de claves, y en cada iteración, el diccionario se actualiza para acceder a la siguiente clave.
Si la clave no existe o se produce un error de tipo, la función devuelve None.
Si todo va bien, la función devuelve el valor final como una cadena de texto.
2. get_res(s, paths)
Propósito: Esta función toma una lista de cadenas JSON (s) y una lista de rutas (paths), y devuelve una lista con los valores correspondientes a esas rutas.
Detalles:
Primero, la función junta todas las cadenas en la lista s en una sola cadena y la convierte en un diccionario usando json.loads().
Luego, para cada ruta en paths, utiliza get_dict_value para obtener el valor correspondiente en el diccionario.
Si get_dict_value devuelve None, agrega "None" a la lista de resultados; de lo contrario, agrega el valor encontrado.
Finalmente, devuelve la lista de resultados.
3. Bloque principal
Propósito: Ejecuta el código cuando se ejecuta el script.
Detalles:
Se define un objeto JSON s, que es una lista con una sola cadena que representa un diccionario con un coche (car) con wheels y gears.
Luego, el usuario debe ingresar el número de rutas (paths_count) y las rutas de acceso correspondientes.
Se llama a get_res con s y las rutas ingresadas, y los resultados se imprimen.
Ejemplo de Ejecución:
Supongamos que el usuario ingresa 2 y luego las rutas car.wheels y car.gears, la salida sería:
