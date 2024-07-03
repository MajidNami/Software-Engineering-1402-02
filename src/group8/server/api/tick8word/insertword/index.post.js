import {createWord, getWordByUserWord} from "../../../db/insert";

export default defineEventHandler(async (event) => {
    //user auth is not indicated
    //  const userId = event.context.auth?.user2.id
    const userId = 1;
    const {word} = await readBody(event);

    try {
        //validation
        if (word.length > 30 || word.length < 3) {
            return createError({statusCode: 402, statusMessage: 'name most be lower than 30 or biger than 3'})
        }
        const data = await $fetch(`https://api.dictionaryapi.dev/api/v2/entries/en/${word}`).catch((error) => {
            return createError({
                statusCode: 407,
                statusMessage: 'input data isnt a valid word or data does not found in database'
            })
        });
        if (data.statusCode == 407) {
            return data
        }
        let dateNew = Date.now() - 40000
        const bar = '' + dateNew;
        const wordOnDataBase = await getWordByUserWord(word, userId)
        if (wordOnDataBase) {
            return createError({statusCode: 408, statusMessage: 'the current word is in active tick8 learning system'})
        }

        return await createWord(userId, word.toLowerCase(),bar);

    } catch (error) {
        return createError({
            statusCode: 500,
            statusMessage: error,
        });
    }
});