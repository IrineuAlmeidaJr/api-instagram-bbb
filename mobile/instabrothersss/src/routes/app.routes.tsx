import {createNativeStackNavigator } from '@react-navigation/native-stack';

const { Navigator, Screen } = createNativeStackNavigator(); 

import { Home } from '../screens/Home'
import { BrotherFollower } from '../screens/BrotherFollower'

export function AppRoutes(){
    return (        
        <Navigator screenOptions={{ headerShown: false }} initialRouteName="home" >                
            <Screen
                name="home"
                component={Home}
            />

            <Screen
                name="brotherfollower"
                component={BrotherFollower}
            />
        </Navigator>
    );
}