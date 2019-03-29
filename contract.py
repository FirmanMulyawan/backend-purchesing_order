from flask import Flask, jsonify, request
from app import app, db
from model import Contract


@app.route('/contract')
def tesContract():
    return 'tes koneksi Contract'

# ========================================== ADD CONTRACT =====================================
@app.route('/addContract', methods=["POST"])
def add_contract():

    body = request.json

    vendor_name = body['vendor_name']
    contract_start_date = body['contract_start_date']
    contract_end_date = body['contract_end_date']
    currency = body['currency']
    plant = body['plant']


    try:
        contract = Contract(
            vendor_name = vendor_name,
            contract_start_date = contract_start_date,
            contract_end_date = contract_end_date,
            currency = currency,
            plant = plant,
        )

        db.session.add(contract)
        db.session.commit()
        return "add contract. contract id={}".format(Contract.contract_id), 200

    except Exception as e:
        return(str(e)), 400

# ========================================== GET ALL CONTRACT =======================
@app.route('/getAllContract', methods=["GET"])
def get_all_contract():
        try:
                contract = Contract.query.order_by(Contract.contract_id).all()
                return jsonify([usr.serialize()
                for usr in contract])
        except Exception as e:
                return (str(e))

# ================================== GET CONTRACT BY ======================================
@app.route('/getContractBy/<contractId_>', methods=["GET"])
def get_contract_by(contractId_):
        try:
                contract = Contract.query.filter_by(contract_id=contractId_).first()
                return jsonify(contract.serialize())
        except Exception as e:
                return (str(e))

# =============================== UPDATE CONTRACT ==========================================
@app.route('/updateContract/<contractId_>', methods=["PUT"])
def update_contract(contractId_):

        body = request.json
        contract_existing = get_contract_by(contractId_).json

        if 'vendor_name' not in body:
                vendor_name = contract_existing['vendor_name']
        else:
                vendor_name = body['vendor_name']
        if 'contract_start_date' not in body:
                contract_start_date = contract_existing['contract_start_date']
        else:
                contract_start_date = body['contract_start_date']
        if 'contract_end_date' not in body:
                contract_end_date = contract_existing['contract_end_date']
        else:
                contract_end_date = body['contract_end_date']
        if 'currency' not in body:
                currency = contract_existing['currency']
        else:
                currency = body['currency']
        if 'plant' not in body:
                plant = contract_existing['plant']
        else:
                plant = body['plant']
        try:
                contractUpdate = {
                    'vendor_name': vendor_name,
                    'contract_start_date': contract_start_date,
                    'contract_end_date': contract_end_date,
                    'currency': currency,
                    'plant': plant,

                }
                contract = Contract.query.filter_by(contract_id=contractId_).update(contractUpdate)
                db.session.commit()
                return 'update contract'
        except Exception as e:
                return(str(e))

                