from app import app
from app.models.supplier import *
from app.models.barang import *
from flask import session, render_template, redirect, url_for, request

@app.route('/data-supplier')
def bossDataSupplier():
    if 'loggedin' in session:
        if session['role'] == 1 :
            
            getSupplier = Supplier().selectSupplier()
            
            return render_template('menu/data_supplier.html', dataSupplier=getSupplier)
        
        else :
            return redirect(url_for('dashboard'))
        
    return redirect(url_for('login'))

@app.route('/data-supplier/store', methods=['POST'])
def bossDataSupplierStore():
    if session['role'] == 1:
        if request.method == 'POST' and 'nama_suplier' in request.form and 'nomor_telepon' in request.form and 'status' in request.form and 'alamat' in request.form and 'email' in request.form:
            nama_suplier = request.form['nama_suplier']
            nomor_telepon = request.form['nomor_telepon']
            status = request.form.getlist('status')
            alamat = request.form['alamat']
            email = request.form['email']

            Supplier().insertSupplier(nama_suplier, nomor_telepon, status, alamat, email)

            return redirect(url_for('bossDataSupplier'))
        
    else :
        return redirect(url_for('dashboard'))

    return redirect(url_for('login'))

@app.route('/data-supplier/detail/<int:id>', methods = ['GET'])
def bossDataSupplierOne(id):
    if 'loggedin' in session:
        if session['role'] == 1 :
            getSupplierOne = Supplier().selectSupplierOne(id)
            getBarangSupplier = Barang().selectBarangSupplier(id)

            return render_template('menu/data_supplier_detail.html', dataSupplierOne=getSupplierOne, dataBarangSupplier=getBarangSupplier)

        else :
            return redirect(url_for('dashboard'))

    return redirect(url_for('login'))

@app.route('/data-supplier/detail/update', methods =['POST'])
def bossDataSupplierUpdate():
    if 'loggedin' in session:
        if session['role'] == 1 :
            if request.method == 'POST' and 'nama_suplier' in request.form and 'nomor_telepon' in request.form and 'status' in request.form and 'alamat' in request.form and 'email' in request.form:
                id = request.form['id']
                nama_suplier = request.form['nama_suplier']
                nomor_telepon = request.form['nomor_telepon']
                status = request.form.getlist('status')
                alamat = request.form['alamat']
                email = request.form['email']

                Supplier().updateSupplier(id, nama_suplier, nomor_telepon, status, alamat, email)

                return redirect(url_for('bossDataSupplier'))

        else :
            return redirect(url_for('dashboard'))
        
    return redirect(url_for('login'))

@app.route('/data-supplier/destroy/<int:id>', methods = ['GET'])
def bossDataSupplierDelete(id):
    if 'loggedin' in session:
        if session['role'] == 1 :
            getSupplier = Supplier().selectSupplier()
            # data = 
            Supplier().deleteSupplier(id)
            
            return redirect(url_for('bossDataSupplier'))

        else :
            return redirect(url_for('dashboard'))
        
    return redirect(url_for('login'))