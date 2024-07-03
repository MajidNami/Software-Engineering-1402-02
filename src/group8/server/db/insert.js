import {prisma} from ".";

export async function createWord(userId, word,reminder) {
    try {
        const Word = await prisma.tick8Word.create({
            data: {
                userId,
                word,
                reminder
            }
        });
        return Word;
    } catch (error) {
        console.error('Error creating word: ', error);
        throw error;
    }
}

export async function getAllUserWord(userId,archive) {
    try {
        return await prisma.tick8Word.findMany({
            where: {userId, archive: archive,
            },
        });
    } catch (error) {
        console.error('Error retrieving words: ', error);
        throw error;
    }
}


export async function getWordById(id) {
    try {
        return await prisma.tick8Word.findUnique({
            where: {id},
        });
    } catch (error) {
        console.error('Error retrieving word: ', error);
        throw error;
    }
}


export async function getWordByUserWord(word, userId) {
    try {
        return await prisma.tick8Word.findFirst({
            where: {
                AND: [
                    {word: word},
                    {userId: userId}
                ]
            }
        });
    } catch (error) {
        console.error('Error retrieving word: ', error);
        throw error;
    }
}

export async function updateWord(id, count, correct, wrong, reminder, archive) {
    try {
        return await prisma.tick8Word.update({
            where: {id},
            data: {
                count,
                correct,
                wrong,
                reminder,
                archive
            },
        });
    } catch (error) {
        console.error('Error updating word: ', error);
        throw error;
    }
}

//archive instead
export async function deleteWord(id) {
    try {
        return await prisma.tick8Word.delete({
            where: {id},
        });
    } catch (error) {
        console.error('Error deleting words: ', error);
        throw error;
    }
}