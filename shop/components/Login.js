import React, { useState } from 'react';
import { View, Text } from 'react-native';
import { TextInput } from 'react-native-gesture-handler';


export const Login = () => {
    const [usuario, onChangeUser] = useState('');
    const [pass, onChangePass] = useState('');
    const label_user = 'Usuario';
    const label_pass = 'Contraseña';

    return (
        <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
            <Text>{label_user}</Text>
            <TextInput style={{ height: 40, borderRadius: 20, borderWidth: 1, padding: 5 }}
                value={usuario} onChangeText={usuario => onChangeUser(usuario)}
            ></TextInput>
                <Text>{label_pass}</Text>
                <TextInput style={{ height: 40, borderRadius: 20, borderWidth: 1, padding: 5 }}
                    value={pass} onChangeText={pass => onChangePass(pass)}></TextInput>
            
        </View>
    )
}