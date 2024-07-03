<script setup>
import {onMounted, reactive, ref, watch} from 'vue';
import {useToast} from "primevue/usetoast";

const toast = useToast();

const {data} = await useFetch('/api/tick8word/insertword')

let visibleBottom = ref(false);
let visible = ref(false)
const layout = ref('list');
const newWord = ref(null);
const wordList = ref([])
const wordListLength = computed(() => wordList.value.length)

const sortKey = ref(null);
const sortOrder = ref(null);
const sortField = ref(null);
const response = ref(null)
const error = ref(null)

let TestedWordId = ref(null)

if (data) {
  data.value?.forEach(word => wordList.value.push(word))
}

const sortOptions = ref([
  {label: 'ازمون های فعال', value: 'reminder'},
  {label: 'بیشترین اشتباهات', value: '!wrong'},
  {label: 'بیشترین دفعات ازمون', value: '!count'},
  {label: 'براساس الفبا', value: 'word'}
]);

const onSortChange = (event) => {
  const value = event.value.value;
  const sortValue = event.value;

  if (value.indexOf('!') === 0) {
    sortOrder.value = -1;
    sortField.value = value.substring(1, value.length);
    sortKey.value = sortValue;
  } else {
    sortOrder.value = 1;
    sortField.value = value;
    sortKey.value = sortValue;
  }
};

//add word
async function addWord(word) {
  try {
    const {data: todos, error: err} = await useFetch('/api/tick8word/insertword', {
      method: 'POST',
      body: {
        "word": word
      }
    })
if (todos.value){
  toast.add({severity: 'success', summary: 'افزوده شد', detail: ` با موفقیت ثبت شد ${todos.value.word} کلمه`, life: 3000});
  const data = wordList.value.push(todos.value);
}else{
  toast.add({severity: 'error', summary: 'ناموفق ', detail: 'کلمه نامفهوم یا در پایگاه داده یافت نشد', life: 3000});

}

  } catch (err) {
    console.log(err)
    toast.add({severity: 'error', summary: 'ناموفق ', detail: 'کلمه نامفهوم یا در پایگاه داده یافت نشد', life: 3000});
  }
}


//run test
let audioUrlUS = ref('')
let audioUrlUK = ref('')
const singleData = ref(null)
const meanings = ref(null)

async function GetTheTest(id) {

  try {
    // Use useFetch to fetch data from the API
    let {data: fetchData, error: fetchError} = await useFetch(`/api/tick8word/insertword/${id}`, {
      key: id.toString(), // Ensure each request is unique based on the ID
      initialCache: false // Force fresh fetch every time
    })
    visibleBottom.value = true
    singleData.value = fetchData.value
    if (singleData.value[0].phonetics[0]) {
      audioUrlUS.value = fetchData.value[0].phonetics[0].audio
      console.log(audioUrlUS.value)
    }
    if (singleData.value[0].phonetics[1]) {
      audioUrlUK.value = fetchData.value[0].phonetics[1].audio
    }

    meanings.value = fetchData.value[0].meanings
    TestedWordId.value = id
    console.log(TestedWordId.value)
  } catch (err) {
    // Assign the error if any
    toast.add({severity: 'error', summary: 'ناموفق ', detail: 'خطا ', life: 3000});
    console.log(err)
  }
}

const audioElementUS = ref(null)
const audioElementUK = ref(null)


const playAudioUK = () => {
  if (audioElementUK.value) {
    audioElementUK.value.play()
  }
}
const playAudioUS = () => {
  if (audioElementUS.value) {
    audioElementUS.value.play()
  }
}

const wordUserInput = ref(null)

//post the word we want
async function iDontKnow(id) {

  try {
    const {data: todo, error: error} = await $fetch(`/api/tick8word/insertword/${TestedWordId.value}`, {
      method: 'POST',
      body: {
        "word": "lolalalalalalalalala"
      }
    })
    const {data} = await useFetch('/api/tick8word/insertword')
    wordList.value = []
    data.value?.forEach(word => wordList.value.push(word))
    visibleBottom.value = false;
    visible.value = false
    toast.add({severity: 'warn', summary: 'غلط', detail: ` اشکالی نداره عزیزم فردا دوباره تلاش کن`, life: 3000});

  } catch (err) {
    toast.add({severity: 'error', summary: 'خطا', detail: `خطا`, life: 3000});
  }


}

async function thePostThatUserGive(word) {
  try {
    const {data: well, error: error,} = await $fetch(`/api/tick8word/insertword/${TestedWordId.value}`, {
      method: 'POST',
      body: {
        "word": word
      }
    })
    const {data} = await useFetch('/api/tick8word/insertword')
    wordList.value = []
    data.value?.forEach(word => wordList.value.push(word))
    visibleBottom.value = false;
    visible.value = false
    wordUserInput.value = null
    toast.add({severity: 'info', summary: '', detail: ` !درست بود، فردا می‌بینمت`, life: 3000});

  } catch (err) {

  }


}

</script>

<template>
  <Toast/>
  <Sidebar v-model:visible="visibleBottom" position="bottom" style="height: 100%">
    <div class="grid">
      <Card class="col-12 md:col-6 md:m-auto ">
        <template #header>
        </template>
        <template #title>
          <div class="grid justify-content-between">


            <div class="">{{ singleData[0].word }}</div>

            <div class="grid gap-2">

              <Button icon="pi pi-volume-up" @click="playAudioUK" label="UK" aria-label="User" v-if="audioUrlUK"/>
              <Button icon="pi pi-volume-up" @click="playAudioUS" label="US" aria-label="User" v-if="audioUrlUS"/>
              <audio ref="audioElementUK" class="hidden" :src="audioUrlUK"></audio>
              <audio ref="audioElementUS" class="hidden" :src="audioUrlUS"></audio>

            </div>


          </div>
        </template>
        <template #subtitle>{{ singleData[0].phonetic }}</template>
        <template #content>
          <div style="min-height: 60vh;">
            <div class="text-lg font-bold">معانی:</div>

            <Accordion :activeIndex="0">
              <AccordionTab v-for="meaning in meanings" :key="meaning.index" :header="meaning.partOfSpeech">

                <p class="m-0" v-for="definition in meaning.definitions" :key="definition.index">
                  :::{{ definition.definition }}</p>

              </AccordionTab>
            </Accordion>

          </div>

        </template>
        <template #footer>
          <div class="flex gap-4 mt-1">
            <Button label="بازگشت" severity="secondary" outlined class="w-full" @click="visibleBottom=false"/>
            <Button label="اجرای آزمون" class="w-full" @click="visible=true"/>
          </div>
        </template>
      </Card>

    </div>
  </Sidebar>
  <Sidebar v-model:visible="visible" header="Sidebar" position="full">
    <Card class="col-12 md:col-6 md:m-auto ">
      <template #header>
      </template>
      <template #title>
        <div class="grid justify-content-between">
          <div class="">آزمون</div>
          <div class="grid gap-2">

            <Button icon="pi pi-volume-up" @click="playAudioUK" label="UK" aria-label="User" v-if="audioUrlUK"/>
            <Button icon="pi pi-volume-up" @click="playAudioUS" label="US" aria-label="User" v-if="audioUrlUS"/>
            <audio ref="audioElementUK" class="hidden" :src="audioUrlUK"></audio>
            <audio ref="audioElementUS" class="hidden" :src="audioUrlUS"></audio>

          </div>


        </div>
      </template>
      <template #subtitle>{{ singleData[0].phonetic }}</template>
      <template #content>
        <div style="min-height: 30vh;" class="mt-8">

          <FloatLabel class="">
            <InputText id="username" v-model="wordUserInput"/>
            <label for="username">کلمه</label>
          </FloatLabel>

        </div>

      </template>
      <template #footer>
        <div class="flex gap-4 mt-1">
          <Button label="نمیدانم" severity="secondary" outlined class="w-full" @click="iDontKnow(TestedWordId)"/>
          <Button label="ثبت" class="w-full" @click="thePostThatUserGive(wordUserInput,TestedWordId)"/>
        </div>
      </template>
    </Card>


  </Sidebar>
  <div class="grid ">
    <div class="col-12 lg:col-6 xl:col-3">
      <div class="card mb-0">
        <div class="flex justify-content-between mb-3">
          <div>
            <span class="block text-500 font-medium mb-3">کلمات</span>
            <div class="text-900 font-medium text-xl">{{ wordListLength }}</div>
          </div>
          <div class="flex align-items-center justify-content-center bg-blue-100 border-round"
               style="width: 2.5rem; height: 2.5rem">
            <i class="pi pi-inbox text-blue-500 text-xl"></i>
          </div>
        </div>
        <nuxt-link to="/archive">
          <span class="text-green-500 font-medium">برای دیدن ارشیو کلیک کنید </span>
        </nuxt-link>
      </div>
    </div>
    <div class="col-12 lg:col-6 xl:col-4">
      <div class="card mb-0">
        <div class="flex justify-content-between mb-2">
          <div>
            <span class="block text-500 font-medium mb-3">افزودن کلمه</span>
            <div class="formgroup-inline">
              <div class="field">
                <label for="firstname1" class="p-sr-only">کلمه</label>
                <InputText id="firstname1" type="text" placeholder="کلمه جدید را وارد کنید" v-model="newWord"/>
              </div>

              <Button label="ثبت" @click="addWord(newWord)"></Button>
            </div>
          </div>
        </div>

      </div>
    </div>
    <div class="col-12">
      <div class="card">
        <h5>لیست کلمات</h5>

        <DataView :value="wordList" :layout="layout" :paginator="true" :rows="9" :sortOrder="sortOrder"
                  :sortField="sortField">
          <template #header>
            <div class="grid grid-nogutter">
              <div class="col-6 text-left">
                <Dropdown v-model="sortKey" :options="sortOptions" optionLabel="label" placeholder="مرتب سازی"
                          @change="onSortChange($event)"/>
              </div>

            </div>
          </template>

          <template #list="slotProps">
            <div class="grid grid-nogutter">
              <div v-for="(item, index) in slotProps.items" :key="index" class="col-12">
                <div class="flex flex-column sm:flex-row sm:align-items-center p-4 gap-3"
                     :class="{ 'border-top-1 surface-border': index !== 0 }">

                  <div class="flex flex-column md:flex-row justify-content-between md:align-items-center flex-1 gap-4">
                    <div class="flex flex-row md:flex-column justify-content-between align-items-start gap-2">
                      <div class="mb-4 ">
                        <span class="font-medium text-lg text-900 ">{{ item.word }}</span>
                      </div>

                      <div class="grid gap-2 ">
                        <div class="surface-100 p-1" style="border-radius: 30px">
                          <div class="surface-0 flex align-items-center gap-2 justify-content-center py-1 px-2"
                               style="border-radius: 30px; box-shadow: 0px 1px 2px 0px rgba(0, 0, 0, 0.04), 0px 1px 2px 0px rgba(0, 0, 0, 0.06)">
                            <span class="text-900 font-medium text-sm">{{ item.correct }}</span>
                            <i class="pi pi-check-circle text-green-500"></i>
                          </div>
                        </div>
                        <div class="surface-100 p-1" style="border-radius: 30px">
                          <div class="surface-0 flex align-items-center gap-2 justify-content-center py-1 px-2"
                               style="border-radius: 30px; box-shadow: 0px 1px 2px 0px rgba(0, 0, 0, 0.04), 0px 1px 2px 0px rgba(0, 0, 0, 0.06)">
                            <span class="text-900 font-medium text-sm">{{ item.wrong }}</span>
                            <i class="pi pi-ban text-red-500"></i>
                          </div>
                        </div>
                        <div class="surface-100 p-1" style="border-radius: 30px">
                          <div class="surface-0 flex align-items-center gap-2 justify-content-center py-1 px-2"
                               style="border-radius: 30px; box-shadow: 0px 1px 2px 0px rgba(0, 0, 0, 0.04), 0px 1px 2px 0px rgba(0, 0, 0, 0.06)">
                            <span class="text-900 font-medium text-sm">{{ item.count }}</span>
                            <i class="pi pi-hourglass text-white-500"></i>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div class="flex flex-column md:align-items-end gap-5">
                      <span class="text-xl font-semibold text-900" v-if="item.reminder-Date.now()>0">  {{
                          Math.round((item.reminder - Date.now()) / 3600000)
                        }}H </span>

                      <div class="flex flex-row-reverse md:flex-row gap-2">


                        <Button icon="pi pi-book" label="تست بده" class="flex-auto md:flex-initial white-space-nowrap"
                                v-if="item.reminder-Date.now()<0" @click="GetTheTest(item.id)"></Button>

                        <Button icon="pi pi-calendar" label="هنوز وقتش نشده" disabled
                                class="flex-auto md:flex-initial white-space-nowrap " v-else></Button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </template>
        </DataView>
      </div>
    </div>


  </div>
</template>
