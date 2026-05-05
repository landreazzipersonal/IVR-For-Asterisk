validates CPF format<br>
strips dots/dashes automatically<br>
rejects repeated digits (11111111111, etc.)<br>
calculates check digits correctly<br>
returns values to Asterisk as channel variables<br>
<br>
Make it executable:<br>
chmod +x agi/validate_cpf.py<br>
<br>
Path:<br>
/var/lib/asterisk/agi-bin/validate_cpf.py<br>
