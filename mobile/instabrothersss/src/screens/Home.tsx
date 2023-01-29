import { View, Text, TouchableOpacity } from "react-native";
import { Feather } from "@expo/vector-icons"
import { useNavigation } from '@react-navigation/native'

import colors from 'tailwindcss/colors'

export function Home() {
    const { navigate } = useNavigation();

    return (
        <View className="flex-1 bg-background px-8 pt-16 justify-center items-center">
            <Text className="text-white">
                Home
            </Text>

            <TouchableOpacity
                activeOpacity={0.7}
                className="m-4 flex-row h-11 px-4 border border-white bg-slate-100 rounded-lg items-center"
                onPress={() => navigate('brotherfollower')}
            >
                < Feather 
                    name="arrow-up"
                    color={colors.gray[500]}
                    size={20}
                />

                <Text className="text-gray-500 ml-3 font-semibold text-base">
                    Novo
                </Text>

            </TouchableOpacity>

        </View>
    )
}