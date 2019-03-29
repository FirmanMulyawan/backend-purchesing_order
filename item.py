from flask import Flask, jsonify, request
from app import app, db
from model import Item


@app.route('/item')
def tesItem():
    return 'tes koneksi Item'

# ============================================ ADD ITEM ==============================
@app.route('/addItem', methods=["POST"])
def add_item():

    body = request.json
    item_type = body['item_type']
    material = body['material']
    description = body['description']
    storage_location = body['storage_location']
    quantity = body['quantity']
    price_each = body['price_each']
    budget_source = body['budget_source']
    note = body['note']

    try:
        item = Item(
            item_type= item_type,
            material=material,
            description= description,   
            storage_location= storage_location,
            quantity= quantity,
            price_each= price_each,
            budget_source= budget_source,
            note= note
        )

        db.session.add(item)
        db.session.commit()
        return "add item. item id={}".format(item.item_id), 200

    except Exception as e:
        return(str(e)), 400

# ========================================== GET ALL ITEM ================================
@app.route('/getAllItem', methods=["GET"])
def get_all_item():
        try:
                item = Item.query.order_by(Item.item_id).all()
                return jsonify([usr.serialize()
                                for usr in item])
        except Exception as e:
                return (str(e))

# ============================================ GET ITEM BY =====================================
@app.route('/getItemBy/<itemId_>', methods=["GET"])
def get_item_by(itemId_):
        try:
                item = Item.query.filter_by(item_id=itemId_).first()
                return jsonify(item.serialize())
        except Exception as e:
                return (str(e))

# =============================================== UPDATE ITEM =====================================
@app.route('/updateItem/<itemId_>', methods=["PUT"])
def update_item(itemId_):

        body = request.json
        item_existing = get_item_by(itemId_).json

        if 'item_type' not in body:
                item_type = item_existing['item_type']
        else:
                item_type = body['item_type']
        if 'material' not in body:
                material = item_existing['material']
        else:
                material = body['material']
        if 'description' not in body:
                description = item_existing['description']
        else:
                description = body['description']
        if 'storage_location' not in body:
                storage_location = item_existing['storage_location']
        else:
                storage_location = body['storage_location']
        if 'quantity' not in body:
                quantity = item_existing['quantity']
        else:
                quantity = body['quantity']
        if 'price_each' not in body:
                price_each = item_existing['price_each']
        else:
                price_each = body['price_each']
        if 'budget_source' not in body:
                budget_source = item_existing['budget_source']
        else:
                budget_source = body['budget_source']
        if 'note' not in body:
                note = item_existing['note']
        else:
                note = body['note']
        try:
                itemUpdate = {
                    'item_type': item_type,
                    'material': material,
                    'description': description,
                    'storage_location': storage_location,
                    'quantity': quantity,
                    'price_each': price_each,
                    'budget_source': budget_source,
                    'note': note,


                }
                item = Item.query.filter_by(item_id=itemId_).update(itemUpdate)
                db.session.commit()
                return 'update item'
        except Exception as e:
                return(str(e))