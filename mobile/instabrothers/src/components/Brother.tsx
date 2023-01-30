import { useNavigation } from '@react-navigation/native'
import { Text, View, Dimensions, TouchableOpacity, Image} from "react-native";

const BROTHERS_LINE = 2;
const SCREEN_HORIZONTAL_PADDING = (16 * 2);

export const BROTHERS_MARGIN_BETWEEN = 8;

export const DAY_SIZE = (Dimensions.get('screen').width / BROTHERS_LINE) - (SCREEN_HORIZONTAL_PADDING + 16);

interface Brother {
    name: string;
    user_instagram: string;
    followers_before: number;
    followers_current: number;
    url_img: string;
}

export function Brother(brother: Brother) {
    const { navigate } = useNavigation();
    //console.log(brother.url_img);

    return (
        <View className="flex-col justify-center items-center my-2">        
            <TouchableOpacity 
                className="m-2 rounded-full justify-center items-center"
                style={{width: DAY_SIZE, height: DAY_SIZE}}
                activeOpacity={0.7}
                onPress={() => navigate(
                    'detailsbrother', 
                    {
                        name: brother.name,
                        user_instagram: brother.user_instagram,
                        followers_before: brother.followers_before,
                        followers_current: brother.followers_current,
                        url_img: brother.url_img
                    }                    
                )}
            >
                <View className='rounded-full border-4 border-background'>
                    <Image 
                        className="bg-white rounded-full"
                        style={{width: DAY_SIZE, height: DAY_SIZE}}
                        source={{
                            uri: brother.url_img,
                        }}
                    />
                </View>                
            </TouchableOpacity>
            <Text
                className="text-white text-lg font-semibold text-center mx-1"
            >
                {brother.name}
            </Text>
        </View>
    )
}