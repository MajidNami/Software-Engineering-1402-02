import {getWordById, updateWord} from "../../../db/insert";

export default defineEventHandler(async (event) => {
    //user auth is not indicated
    //  const userId = event.context.auth?.user2.id
    //const userId = 1;
    const wordId = event.context.params.word;
    console.log(wordId)
    const {word} = await readBody(event);
    try {
        //validation
        if (word.length > 30 || word.length < 3) {
            return createError({statusCode: 402, statusMessage: 'word most be lower than 30 or bigger than 3'})
        }
        const DBWord = await getWordById(parseInt(wordId))
        if (!DBWord || DBWord.archive == true ) {
            return createError({statusCode: 402, statusMessage: 'word does not exist as active user tick8 program'})
        }

        const {correct, count, reminder, wrong} = DBWord

        if (reminder > Date.now()) {
            return createError({
                statusCode: 408,
                statusMessage: `once a day u can practice the word so come back at ${new Date(Number(reminder))}`
            })
        }
        let dateNew = Date.now() + 86400000
        const bar = '' + dateNew;

        if (word.toLowerCase() == DBWord.word) {
            if (correct + 1 == 8)
            {
             return await updateWord(parseInt(wordId), count + 1, correct + 1, wrong, bar,true)
            }
            return await updateWord(parseInt(wordId), count + 1, correct + 1, wrong, bar)
        }
            return await updateWord(parseInt(wordId), count + 1, correct, wrong + 1, bar)

    } catch (error) {
        return createError({
            statusCode: 500,
            statusMessage: error,
        });
    }
});