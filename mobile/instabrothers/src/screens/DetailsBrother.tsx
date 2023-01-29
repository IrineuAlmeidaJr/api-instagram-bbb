import { useRoute } from "@react-navigation/native";
import { View, Text, StyleSheet } from "react-native";
import { Brother } from "../components/Brother";

import { Header } from "../components/Header";

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

    return (
        <View className="flex-1 bg-background px-4 pt-12 justify-center items-center">
            <Header />
            <View className="mt-8 flex-1 items-center">
                <Brother 
                     key={`${brother}-1`} 
                     name={brother.name} 
                     user_instagram={brother.user_instagram}
                     followers_before={brother.followers_before}
                     followers_current={brother.followers_current}
                     url_img={brother.url_img}
                />
                <Text className="ml-4 text-white font-semibold text-lg">
                    {brother.user_instagram}
                </Text>
                <Text className="ml-4 text-white font-semibold text-lg">
                    Antes: {brother.followers_before.toLocaleString()}
                </Text>
                <Text className="ml-4 text-white font-semibold text-lg">
                    Atual: {brother.followers_current.toLocaleString()}
                </Text>
            </View>
        </View>
    )
}