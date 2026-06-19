import React, { useState } from 'react';

// 1. 資料庫區域
const FLOWER_OPTIONS = ["厄瓜多玫瑰", "奧斯汀玫瑰", "太陽玫瑰", "康乃馨", "牡丹", "繡球花", "庭園玫瑰", "向日葵", "大理花", "鬱金香", "蓮花", "百合", "小蒼蘭", "雞冠花", "洋桔梗", "風信子", "乒乓菊", "蝴蝶蘭", "星辰花", "陸蓮", "海芋", "紅掌", "大波斯菊", "香水百合", "非洲菊", "龍膽花", "鈴蘭", "鐵線蓮", "罌粟花", "無"];
const AUX_OPTIONS = ["滿天星", "卡斯比亞", "兔尾草", "加那利草", "臘梅", "黃金球", "不凋金合歡", "薰衣草", "千日紅", "麥桿菊", "珍珠草", "勿忘我", "紫薊", "薊花", "小雛菊", "澳洲臘梅", "鼠尾草", "藍星花", "小米果", "尤加利果", "山防風", "繡線菊", "蕨類花穗", "高粱", "白梅", "蠟菊", "銀蓮花", "石斛蘭", "火龍珠", "無"];
const LEAF_OPTIONS = ["圓葉尤加利", "細葉尤加利", "銀葉桉", "黃金葛", "雪花蕨", "大葉蕨", "鐵線蕨", "腎蕨", "雪松", "扁柏", "苔蘚", "網狀葉", "芒草", "枯枝", "空氣鳳梨", "黃金樹葉", "斑葉蘭", "常春藤", "橡膠樹葉", "棕櫚葉", "補血草葉", "百里香", "迷迭香", "武竹", "蘆葦", "狗尾草", "乾燥草繩", "樺木片", "尤加利種子", "無"];
const WRAP_OPTIONS = ["霧面紙", "反光紙", "金屬紙", "薄紗", "牛皮紙"];

// 2. 獨立組件：單一花材選擇區塊
const FlowerSelector = ({ label, options, onChange }) => (
  <div className="flex gap-2 mb-2">
    <select onChange={(e) => onChange(e.target.value)} className="flex-1 p-2 border rounded">
      <option value="">選擇{label}</option>
      {options.map(item => <option key={item} value={item}>{item}</option>)}
    </select>
    <input type="color" className="w-12 h-10 border rounded cursor-pointer" />
  </div>
);

export default function FlowerApp() {
  const [design, setDesign] = useState({
    type: '盆花',
    mains: { A: '', B: '', C: '' },
    auxs: { A: '', B: '' },
    leafs: { A: '', B: '' },
    wrap: ''
  });
  const [prompt, setPrompt] = useState('');

  const generatePrompt = () => {
    const p = `Professional preserved flower ${design.type}, featuring ${design.mains.A}, ${design.mains.B}, ${design.mains.C}, accented with ${design.auxs.A}, ${design.auxs.B} and ${design.leafs.A}, ${design.leafs.B}, wrapped in ${design.wrap}, high-end floral design, studio lighting, 8k resolution, photorealistic, soft texture.`;
    setPrompt(p);
  };

  return (
    <div className="max-w-xl mx-auto p-4 bg-white shadow-lg rounded-xl">
      <h2 className="text-xl font-bold mb-4">花藝設計設定</h2>
      
      <div className="mb-6">
        <label className="block font-semibold mb-2">1. 類型</label>
        <select onChange={(e) => setDesign({...design, type: e.target.value})} className="w-full p-2 border rounded">
          <option>盆花</option>
          <option>捧花</option>
        </select>
      </div>

      <div className="mb-4">
        <label className="block font-semibold mb-2">2. 主花 (A/B/C)</label>
        <FlowerSelector label="主花A" options={FLOWER_OPTIONS} onChange={(v) => setDesign({...design, mains: {...design.mains, A: v}})} />
        <FlowerSelector label="主花B" options={FLOWER_OPTIONS} onChange={(v) => setDesign({...design, mains: {...design.mains, B: v}})} />
        <FlowerSelector label="主花C" options={FLOWER_OPTIONS} onChange={(v) => setDesign({...design, mains: {...design.mains, C: v}})} />
      </div>

      <div className="mb-4">
        <label className="block font-semibold mb-2">3. 輔助花 (A/B)</label>
        <FlowerSelector label="輔助A" options={AUX_OPTIONS} onChange={(v) => setDesign({...design, auxs: {...design.auxs, A: v}})} />
        <FlowerSelector label="輔助B" options={AUX_OPTIONS} onChange={(v) => setDesign({...design, auxs: {...design.auxs, B: v}})} />
      </div>

      <div className="mb-4">
        <label className="block font-semibold mb-2">4. 葉材 (A/B)</label>
        <FlowerSelector label="葉材A" options={LEAF_OPTIONS} onChange={(v) => setDesign({...design, leafs: {...design.leafs, A: v}})} />
        <FlowerSelector label="葉材B" options={LEAF_OPTIONS} onChange={(v) => setDesign({...design, leafs: {...design.leafs, B: v}})} />
      </div>

      <div className="mt-6 flex gap-2">
        <button onClick={generatePrompt} className="flex-1 bg-blue-600 text-white py-2 rounded">產生題詞</button>
        <button onClick={() => navigator.clipboard.writeText(prompt)} className="bg-gray-700 text-white px-4 py-2 rounded">複製</button>
      </div>
      
      {prompt && <p className="mt-4 text-xs text-gray-500 bg-gray-100 p-2">{prompt}</p>}
    </div>
  );
}
