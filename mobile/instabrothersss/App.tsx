import { SafeAreaView, StatusBar } from 'react-native';
import * as SplashScreen from "expo-splash-screen";
import { 
  useFonts, 
  Inter_400Regular,  
  Inter_600SemiBold,  
  Inter_700Bold,
  Inter_800ExtraBold
} from '@expo-google-fonts/inter';

import { Home } from './src/screens/Home';
import { Routes } from './src/routes';
import { Loading } from './src/components/Loading';
import { useCallback } from 'react';

export default function App() {
  const [fontsLoaded] = useFonts({ 
    Inter_400Regular,  
    Inter_600SemiBold,  
    Inter_700Bold,
    Inter_800ExtraBold
  });

  if(!fontsLoaded) {
    SplashScreen.hideAsync()
    return (
      <Loading/>
    );
  }

  return (
    <>
      <Routes />
      <StatusBar barStyle="dark-content" backgroundColor="transparent" translucent />
    </>
  );
}

