# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""


def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """
    from pathlib import Path
    import pandas as pd
    import os

    train_dir=[
                Path("files/input/input/train/negative"),
                Path("files/input/input/train/positive"),
                Path("files/input/input/train/neutral")
                ]
    
    test_dir=[
            Path("files/input/input/test/negative"),
            Path("files/input/input/test/positive"),
            Path("files/input/input/test/neutral")
            ]
    
    output_dir = Path("files/output")
    
    train_data = []
    test_data = []

    for i in range(0,3):
        for archive in train_dir[i].iterdir():
            if archive.is_file():
                with archive.open("r",encoding="utf-8") as f:
                    content = f.read()
                    if i == 0:
                        result = [content,"negative"]
                    elif i == 1:
                        result = [content,"positive"]
                    else:
                        result = [content,"neutral"]
                        
                    train_data.append(result)

    
    for i in range(0,3):
        for archive in test_dir[i].iterdir():
            if archive.is_file():
                with archive.open("r",encoding="utf-8") as f:
                    content = f.read()
                    if i == 0:
                        result = [content,"negative"]
                    elif i == 1:
                        result = [content,"positive"]
                    else:
                        result = [content,"neutral"]
                        
                    test_data.append(result)
      

    columns = ["phrase","target"]

    df_train= pd.DataFrame(train_data,columns=columns)
    df_test= pd.DataFrame(test_data,columns=columns)


    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    df_train.to_csv(os.path.join(output_dir, "train_dataset.csv"))
    df_test.to_csv(os.path.join(output_dir, "test_dataset.csv"))



pregunta_01()
