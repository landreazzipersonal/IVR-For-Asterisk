
## AGI Scripts<br>
<br>
### validate_cpf.py<br>
<br>
Python AGI script used by Asterisk to validate Brazilian CPF numbers.<br>
<br>
Features:<br>
- removes punctuation automatically<br>
- rejects invalid repeated sequences<br>
- validates CPF check digits<br>
- returns result to the dialplan through channel variables<br>
<br>
Returned variables:<br>
- `CPF_VALIDO`: `SIM` or `NAO`<br>
- `CPF_NORMALIZADO`: digits-only CPF<br>

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

NOTE:<br>
this validates only whether the CPF is mathematically valid.<br>
It does not confirm whether the CPF exists in your database or belongs to a registered caller.<br>

CPF is a brazilian document for citizens, you can use for any document if you adjust for your necessity
