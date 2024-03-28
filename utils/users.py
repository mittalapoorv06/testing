from dbwrapper.connect_database import ConnectDatabase_postgres

def user_signup(user_data):
    name = user_data['name']
    email = user_data['email_id']
    password = user_data['password']
    query = f"INSERT INTO public.users(name, email_id, password) VALUES ('{name}', '{email}', '{password}') RETURNING id"
    db_connection = ConnectDatabase_postgres()
    db_connection.cursor.execute(query)
    
    user_data = db_connection.cursor.fetchone()
    
    print("user_data",user_data)
    db_connection.connection.commit()
    return user_data[0]