import {getAllUserWord} from "../../../db/insert";

export default eventHandler({
    async handler(event) {
        //user auth is not indicated
        //  const userId = event.context.auth?.user2.id
        const userId = 1;
        return await getAllUserWord(userId,false)
    },
})