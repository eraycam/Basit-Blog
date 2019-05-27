from django import forms

class kayitform(forms.Form):
    
    username = forms.CharField(max_length=50,label="Kullanıcı Adı:")
    password = forms.CharField(max_length=50,label="Parola:",widget=forms.PasswordInput)
    confrim = forms.CharField(max_length=50,label="Parolayı Doğrula:",widget=forms.PasswordInput)

    
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confrim = self.cleaned_data.get("confrim")
        

        if password and confrim and password != confrim:
            raise forms.ValidationError("Parola Eşit Değil")
        

        values = {

            "username":username,
            "password":password

        }
        return values

class girisform(forms.Form):
    username = forms.CharField(label = "Kullanıcı Adı")
    password = forms.CharField(label = "Parola",widget = forms.PasswordInput)


        
