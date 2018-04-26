import atws

user = raw_input("Username:")
pass = raw_input("Password:")

at = atws.connect(username=user, password=pass, support_file_path='C:\ATWS\TEMP')

query = atws.Query('Ticket')
query.WHERE('id',query.GreaterThan,5667)
