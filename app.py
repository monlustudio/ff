import React, { useState } from 'react';

// 假設的完整資料庫
const FLOWER_DB = {
  main: ["厄瓜多玫瑰", "奧斯汀玫瑰", "太陽玫瑰", "康乃馨", "牡丹", "繡球花", "無"],
  aux: ["滿天星", "卡斯比亞", "兔尾草", "加那利草", "臘梅", "無"],
  leaf: ["圓葉尤加利", "細葉尤加利", "銀葉桉", "雪松", "苔蘚", "無"],
  wrap: ["霧面紙", "反光紙", "金屬紙", "薄紗", "牛皮紙"]
};

export default function FlowerDesignerApp() {
  const [form, setForm] = useState({
    type: '盆花',
    mainA: { name: '無', color: '#ffffff' },
    mainB: { name: '無', color: '#ffffff' },
    mainC: { name: '無', color: '#ffffff' },
    auxA: { name: '無', color: '#ffffff' },
    auxB: { name: '無', color: '#ffffff' },
    leafA: { name: '無', color: '#ffffff' },
    leafB: { name: '無', color: '#ffffff' },
    wrap: { name: '霧面紙', color: '#ffffff' }
  });

  const [finalPrompt, setFinalPrompt] = useState('');

  // 封裝一個選擇器元件，減少重複代碼
  const SelectionRow = ({ label, category, stateKey, options }) => (
    <div className="flex gap-2 mb-3 items-center">
      <label className="w-24 text-sm font-bold">{label}</label>
      <select 
        className="flex-1 p-2 border rounded"
        onChange={(e) => setForm({...form, [stateKey]: {...form[stateKey], name: e.target.value}})}
      >
        {options.map(item => <option key={item} value={item}>{item}</option>)}
      </select>
      <input 
        type="color" 
        className="w-10 h-10 border-0 cursor-pointer"
        onChange={(e) => setForm({...form, [stateKey]: {...form[stateKey], color: e.target.value}})}
      />
    </div>
  );

  const handleGenerate = () => {
    // 這裡可以加入更精細的邏輯處理「無」的選項
    const p = `Preserved flower ${form.type}, main flowers: ${form.mainA.name}, ${form.mainB.name}, ${form.mainC.name}, accented with ${form.auxA.name}, ${form.auxB.name} and ${form.leafA.name}, ${form.leafB.name}, wrapped in ${form.wrap.name}. High-end commercial photography, 8k, soft lighting.`;
    setFinalPrompt(p);
  };

  return (
    <div className="p-6 max-w-xl mx-auto bg-white shadow-lg rounded-lg">
      <h2 className="text-xl mb-4 border-b pb-2">花藝設計設定</h2>
      
      {/* 結構區 */}
      <div className="mb-4">
        <label className="mr-2">類型:</label>
        <select onChange={(e) => setForm({...form, type: e.target.value})}>
          <option>盆花</option><option>捧花</option>
        </select>
      </div>

      {/* 主花區 */}
      <div className="bg-pink-50 p-3 rounded mb-4">
        <h3 className="font-bold mb-2">主花設定</h3>
        <SelectionRow label="主花 A" stateKey="mainA" options={FLOWER_DB.main} />
        <SelectionRow label="主花 B" stateKey="mainB" options={FLOWER_DB.main} />
        <SelectionRow label="主花 C" stateKey="mainC" options={FLOWER_DB.main} />
      </div>

      {/* 輔助與葉材區 */}
      <div className="bg-green-50 p-3 rounded mb-4">
        <h3 className="font-bold mb-2">配材設定</h3>
        <SelectionRow label="輔助花 A" stateKey="auxA" options={FLOWER_DB.aux} />
        <SelectionRow label="輔助花 B" stateKey="auxB" options={FLOWER_DB.aux} />
        <SelectionRow label="葉材 A" stateKey="leafA" options={FLOWER_DB.leaf} />
        <SelectionRow label="葉材 B" stateKey="leafB" options={FLOWER_DB.leaf} />
      </div>

      {/* 包裝區 */}
      <div className="bg-blue-50 p-3 rounded mb-6">
        <SelectionRow label="包裝材質" stateKey="wrap" options={FLOWER_DB.wrap} />
      </div>

      <div className="flex gap-2">
        <button onClick={handleGenerate} className="bg-blue-600 text-white px-6 py-2 rounded">生成提示詞</button>
        <button onClick={() => navigator.clipboard.writeText(finalPrompt)} className="bg-gray-600 text-white px-6 py-2 rounded">複製</button>
      </div>

      {finalPrompt && <textarea readOnly value={finalPrompt} className="w-full mt-4 p-2 border h-24 text-xs" />}
    </div>
  );
}
