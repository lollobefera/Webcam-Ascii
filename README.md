# Webcam Ascii
## INFO
> Visualizza un ascii art dalla tua webcam in live 🎥<br/>
> Salva uno screen della tua ascii art cliccando la "S" 📷<br/>

## Requisiti
> Interprete Python installato

## Installazione

```sh
- git clone https://github.com/lollobefera/Webcam-Ascii.git

- cd Webcam-Ascii

- pip install -r requirements.txt
```

## Utilizzo

```sh
python start.py
```

## Come funziona?
Le immagini e i video sono delle matrici contenenti i valori RGB da 0 a 255 di ogni pixel (nel caso di OpenCV i valori sono BGR) quindi facendo la media di questi tre valori otteniamo l'intensita di un colore e con questa possiamo disegnare sullo schermo un preciso carattere, per esempio se l'intensità è vicina allo zero il carattere sarà " " e se invece è vicina a 255 sarà "#"

### Librerie
* `OpenCV` - Per catturare il video dalla webcam
* `numpy` - per gestire le matrici
* `pygame` - per visualizzare l'immagine
