import React, { useState } from 'react';

// 1. 完整資料庫清單
const DB = {
  flowers: ["厄瓜多玫瑰", "奧斯汀玫瑰", "太陽玫瑰", "康乃馨", "牡丹", "繡球花", "庭園玫瑰", "向日葵", "大理花", "鬱金香", "蓮花", "百合", "小蒼蘭", "雞冠花", "洋桔梗", "風信子", "乒乓菊", "蝴蝶蘭", "星辰花", "陸蓮", "海芋", "紅掌", "大波斯菊", "香水百合", "非洲菊", "龍膽花", "鈴蘭", "鐵線蓮", "罌粟花", "無"],
  aux: ["滿天星", "卡斯比亞", "兔尾草", "加那利草", "臘梅", "黃金球", "不凋金合歡", "薰衣草", "千日紅", "麥桿菊", "珍珠草", "勿忘我", "紫薊", "薊花", "小雛菊", "澳洲臘梅", "鼠尾草", "藍星花", "小米果", "尤加利果", "山防風", "繡線菊", "蕨類花穗", "高粱", "白梅", "蠟菊", "銀蓮花", "石斛蘭", "火龍珠", "無"],
  leaf: ["圓葉尤加利", "細葉尤加利", "銀葉桉", "黃金葛", "雪花蕨", "大葉蕨", "鐵線蕨", "腎蕨", "雪松", "扁柏", "苔蘚", "網狀葉", "芒草", "枯枝", "空氣鳳梨", "黃金樹葉", "斑葉蘭", "常春藤", "橡膠樹葉", "棕櫚葉", "補血草葉", "百里香", "迷迭香", "武竹", "蘆葦", "狗尾草", "乾燥草繩", "樺木片", "尤加利種子", "無"],
  wraps: ["霧面紙", "反光紙", "金屬紙", "薄紗", "牛皮紙"]
};

export default function FlowerDesignerApp() {
  const [form, setForm] = useState({
    type: '盆花',
    mainA: { name: '厄瓜多玫瑰', color: '#ff0000' },
    mainB: { name: '無', color: '#ffffff' },
    mainC: { name: '無', color: '#ffffff' },
    auxA: { name: '滿天星', color: '#ffffff' },
    auxB: { name: '無', color: '#ffffff' },
    leafA: { name: '圓葉尤加利', color: '#808080' },
    leafB: { name: '無', color: '#ffffff' },
    wrap: { name: '霧面紙', color: '#eeeeee' }
  });

  const [prompt, setPrompt] = useState('');

  const generatePrompt = () => {
    const p = `Professional preserved flower ${form.type}, focal flowers: ${form.mainA.name}, ${form.mainB.name !== '無' ? form.mainB.name : ''}, ${form.mainC.name !== '無' ? form.mainC.name : ''}, accented with ${form.auxA.name !== '無' ? form.auxA.name : ''}, ${form.auxB.name !== '無' ? form.auxB.name : ''}, featuring foliage of ${form.leafA.name}, ${form.leafB.name !== '無' ? form.leafB.name : ''}, wrapped in elegant ${form.wrap.name}. Floral design, commercial product photography, studio lighting, soft depth of field, 8k, photorealistic, premium aesthetic.`;
    setPrompt(p);
  };

  const copyPrompt = () => {
    navigator.clipboard.writeText(prompt);
    alert('提示詞已複製！');
  };

  const InputField = ({ label, keyName, options }) => (
    <div className="flex flex-col mb-3">
      <label className="text-xs font-bold text-gray-600 mb-1">{label}</label>
      <div className="flex gap-2">
        <select 
          className="flex-1 p-2 border rounded text-sm bg-white"
          value={form[keyName].name}
          onChange={(e) => setForm({...form, [keyName]: {...form[keyName], name: e.target.value}})}
        >
          {options.map(o => <option key={o} value={o}>{o}</option>)}
        </select>
        <input type="color" className="w-10 h-9 cursor-pointer" value={form[keyName].color} onChange={(e) => setForm({...form, [keyName]: {...form[keyName], color: e.target.value}})} />
      </div>
    </div>
  );

  return (
    <div className="max-w-md mx-auto p-4 bg-gray-100 min-h-screen font-sans">
      <h1 className="text-xl font-bold text-center mb-4">永生花設計生成器</h1>
      
      <div className="bg-white p-4 rounded-lg shadow-sm">
        <label className="block text-sm font-bold mb-2">花藝類型</label>
        <select className="w-full p-2 border rounded mb-4" onChange={(e) => setForm({...form, type: e.target.value})}>
          <option>盆花</option><option>捧花</option>
        </select>

        <InputField label="主花 A" keyName="mainA" options={DB.flowers} />
        <InputField label="主花 B" keyName="mainB" options={DB.flowers} />
        <InputField label="主花 C" keyName="mainC" options={DB.flowers} />
        <InputField label="輔助花 A" keyName="auxA" options={DB.aux} />
        <InputField label="輔助花 B" keyName="auxB" options={DB.aux} />
        <InputField label="葉材 A" keyName="leafA" options={DB.leaf} />
        <InputField label="葉材 B" keyName="leafB" options={DB.leaf} />
        <InputField label="包裝材質" keyName="wrap" options={DB.wraps} />

        <div className="flex gap-2 mt-6">
          <button onClick={generatePrompt} className="flex-1 bg-pink-600 text-white py-2 rounded font-bold hover:bg-pink-700">生成提示詞</button>
          <button onClick={copyPrompt} className="flex-1 bg-gray-800 text-white py-2 rounded font-bold hover:bg-gray-900">複製</button>
        </div>
      </div>

      {prompt && (
        <div className="mt-4 p-3 bg-white border-l-4 border-pink-500 text-sm italic text-gray-700 shadow-sm">
          {prompt}
        </div>
      )}
    </div>
  );
}
