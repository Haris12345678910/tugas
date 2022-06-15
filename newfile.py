class _rokok():
    def __init__(self, surya, oepet, chef, cahaya_pro, harga_rokok,):
        self.surya = surya
        self.oepet = oepet
        self.chef = chef
        self.cahaya_pro = cahaya_pro
        self.harga_rokok = harga_rokok
        

    def _get (self):
        print('surya   : ' + self.surya)
        print('oepet      : ' + self.oepet + ', ' +  self.oepet)
        if self.chef in ['chef']:
            chef = 'chef'
        else:
            cahaya_pro = 'cahaya_pro'
        print('cahaya_pro      :' + cahaya_pro)

        if self.harga_rokok >20000:
            print('harga_rokok sangat mahal')
        else:
            if self.haga_rokok >20000:
                print('harga_rokok sangat mahal')
            else:
                if self.harga_rokok <20000:
                    print('harga_rokok sangat mahal')

print('=====================================')
print('     PROGRAM HARGA ROKOK      ')
print('=====================================')

surya      = input('surya        :')
oepet = input('oepet        :')
chef  = input('chef       :')
cahaya_pro     = input('cahaya_pro         :')
harga_rokok = float(input('Masukkan harga_rokok :'))

print('======================================')

proses = _rokok(surya,oepet,chef,cahaya_pro,harga_rokok)
print (proses._get())