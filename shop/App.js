import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import { Login } from './components/Login';
import { Provider } from 'react-redux'
import generateStore from './redux/index'


const Stack = createStackNavigator();
const store = generateStore();

function App() {
  const MyTheme = {

    headerStyle: {
      backgroundColor: '#A86AEB',
    },
    headerTintColor: '#fff',
    headerTitleStyle: {
      fontWeight: 'bold',
    },

  };
  return (
    <Provider store={store}>

      <NavigationContainer>
        <Stack.Navigator>
          <Stack.Screen name="Login" component={Login} options={MyTheme} />
        </Stack.Navigator>
      </NavigationContainer>
    </Provider>

  );
}

export default App;
