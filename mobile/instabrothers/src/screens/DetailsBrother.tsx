import { useRoute } from "@react-navigation/native";
import { View, Text, Platform, TouchableOpacity, Linking } from "react-native";




import { Header } from "../components/Header";
import { Brother } from "../components/Brother";
import { Follower } from "../icons/Follower";

interface Brother {
    name: string;
    user_instagram: string;
    followers_before: number;
    followers_current: number;
    url_img: string;
}

export function DetailsBrother(){
    const route = useRoute();
    const brother = route.params as Brother;  

    if(Platform.OS === 'android') { 
        require('intl'); 
        require('intl/locale-data/jsonp/pt-BR'); 
    }

    return (
        <View className="flex-1 bg-background px-4 pt-12 justify-center items-center">
            <Header />
            <View className="mt-8 flex-1 items-center">
                <Brother 
                     key={`${brother}-2`} 
                     name={brother.name} 
                     user_instagram={brother.user_instagram}
                     followers_before={brother.followers_before}
                     followers_current={brother.followers_current}
                     url_img={brother.url_img}
                     isDetailsBrother={false}
                />
                
                <View className="justify-center items-center">
                    <Follower />

                    <View className="flex-row mt-3 justify-center items-center">
                        <Text className="text-white font-semibold text-lg">
                            Antes: {brother.followers_before.toLocaleString('pt-BR')}
                        </Text>

                        <Text className="ml-4 text-white font-semibold text-lg">
                            Atual: { brother.followers_current.toLocaleString('pt-BR')}
                        </Text>
                    </View>
                    
                </View>
                
            </View>
        </View>
    )
}