from flask import Flask, jsonify, request  #importyFlask
import json  #importjson
import os  #importos

app = Flask(__name__)  #tworzenieaplikacjiFlask

DATA_FILE = "tasks.json"  #nazwa/pliku/z/danymi

#WczytywaniezadańzplikuJSON
def load_tasks():  #funkcjawczytujacadane
    if not os.path.exists(DATA_FILE):  #gdypliknieistnieje
        return []  #zwracamylistępustą
    with open(DATA_FILE, "r", encoding="utf-8") as f:  #otwarciedoodczytuUTF8
        return json.load(f)  #parsowanieJSONizrwrótdane

#ZapisywaniezadańdoplikuJSON
def save_tasks(tasks):  #funkcjazapisujacadane
    with open(DATA_FILE, "w", encoding="utf-8") as f:  #otwarciedozapisuUTF8
        json.dump(tasks, f, ensure_ascii=False, indent=2)  #zapiszładniesformatowanyJSON

@app.route("/tasks", methods=["GET"])  #endpointGET/listazadan
def get_tasks():  #handlerGET
    return jsonify(load_tasks())  #zwróclistęzadanwJSON

@app.route("/tasks", methods=["POST"])  #endpointPOST/dodajzadanie
def add_task():  #handlerPOST
    tasks = load_tasks()  #wczytajstanobecny
    data = request.json  #pobierzbodyJSON
    new_task = {  #nowyobiektzadania
        "id": len(tasks) + 1,  #prosteIDinkrementalne
        "title": data.get("title", ""),  #tytułzadaniadomyślniepusty
        "done": False  #statusstartowofalse
    }
    tasks.append(new_task)  #dodajdoListy
    save_tasks(tasks)  #zapiszdoPliku
    return jsonify(new_task), 201  #zwrócutworzonezadanieikod201

@app.route("/tasks/<int:task_id>", methods=["PUT"])  #endpointPUT/aktualizacjazadania
def update_task(task_id):  #handlerPUT
    tasks = load_tasks()  #wczytajdane
    for t in tasks:  #iteracjapozadaniach
        if t["id"] == task_id:  #dopasujpoID
            t["title"] = request.json.get("title", t["title"])  #aktualizujtytułjeślipodany
            t["done"] = request.json.get("done", t["done"])  #aktualizujstatusjeślipodany
            save_tasks(tasks)  #zapiszzmiany
            return jsonify(t)  #zwróczmienionezadanie
    return jsonify({"error": "Task not found"}), 404  #brakIDzwróć404

@app.route("/tasks/<int:task_id>", methods=["DELETE"])  #endpointDELETE/usuwaniezadania
def delete_task(task_id):  #handlerDELETE
    tasks = load_tasks()  #wczytajdane
    new_tasks = [t for t in tasks if t["id"] != task_id]  #odfiltrujusuwaneID
    if len(new_tasks) == len(tasks):  #nicniewyrzucono
        return jsonify({"error": "Task not found"}), 404  #zwróć404
    save_tasks(new_tasks)  #zapisznowąlistę
    return jsonify({"message": "Task deleted"})  #potwierdzenieusunięcia

if __name__ == "__main__":  #uruchomtylkogdypliksamstartuje
    app.run(debug=True)  #włączserwerwtrybiedebug
