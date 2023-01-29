import { View, Text } from "react-native";
import { BackButton } from "../components/BackButton";


export function BrotherFollower() {
    return (
        <View className="flex-1 bg-background px-8 pt-16">
            <View className="flex-row items-center">
                <BackButton />
                <Text className="ml-4 text-white font-semibold">
                    BrotherFollower
                </Text>
            </View>
        </View>
    )
}