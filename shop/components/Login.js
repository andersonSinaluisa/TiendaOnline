import React, { useState } from 'react';
import { View, Text } from 'react-native';
import { TextInput } from 'react-native-gesture-handler';
import { Grid, TextField, Button } from '@material-ui/core';
import { GoogleSignin, GoogleSigninButton } from '@react-native-community/google-signin';

import { app } from '../config/index'
export const Login = () => {



    return (
        <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
            <GoogleSigninButton
                style={{ width: 192, height: 48 }}
                size={GoogleSigninButton.Size.Wide}
                color={GoogleSigninButton.Color.Dark}
                onPress={this._signIn}
                disabled={this.state.isSigninInProgress} />
        </View>
    )
}