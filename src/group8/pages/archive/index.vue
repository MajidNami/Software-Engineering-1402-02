<script setup>
import { ref,} from 'vue';
import {useToast} from "primevue/usetoast";

const toast = useToast();

const {data} = await useFetch('/api/tick8word/insertword/archive')

let visibleBottom = ref(false);
let visible = ref(false)
const layout = ref('list');
const wordList = ref([])
if (data) {
  data.value?.forEach(word => wordList.value.push(word))
}


</script>

<template>

    <div class="col-12">
      <div class="card">
        <h5>لیست کلمات</h5>

        <DataView :value="wordList" :layout="layout" :paginator="true" :rows="12" >
          <template #header>
            <div class="grid grid-nogutter justify-content-end">
              <div class=" text-right ">
                <nuxt-link to="/">
                  <Button label="بازگشت" icon="pi pi-arrow-left" iconPos="right" />
                </nuxt-link>
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

                    </div>
                  </div>
                </div>
              </div>
            </div>
          </template>
        </DataView>
      </div>
    </div>



</template>
