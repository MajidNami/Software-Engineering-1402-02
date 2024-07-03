import { getWordById} from "../../../db/insert";

export default eventHandler({
    async handler(event) {
        //user auth is not indicated
        //  const userId = event.context.auth?.user2.id
        const wordId = event.context.params.word;
       const word= await getWordById(parseInt(wordId))
        if(word.archive == true || !word){
            return createError({statusCode: 402, statusMessage: 'word does not exist as active user tick8 program'})
        }
        if (word.reminder > Date.now()) {
            return createError({
                statusCode: 408,
                statusMessage: `once a day u can practice the word so come back at ${new Date(Number(word.reminder))}`
            })
        }
        const data = await $fetch(`https://api.dictionaryapi.dev/api/v2/entries/en/${word.word}`).catch((error) => {
            return createError({
                statusCode: 407,
                statusMessage: 'input data isnt a valid word or data does not found in database'
            })
        });

       return data
    },
})