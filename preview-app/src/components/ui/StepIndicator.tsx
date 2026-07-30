/**
 * StepIndicator - v8 FINAL (Exact Figma 2-Column Layout)
 */

import React from 'react';

const ICONS = {
  checkCircle: "http://localhost:3845/assets/261172205a0b3f13fef91e2e6515eeb6f277d4bf.svg",
  receipt: "http://localhost:3845/assets/bb36ab6a37793346687ddd0ec5bd8e6616098a0d.svg",
  pencil: "http://localhost:3845/assets/726008d0d0e839bf860a7746d69ba1d95504cc43.svg",
  call: "http://localhost:3845/assets/a97e47b9b059d19d7fd3d9954e43fef818616f2b.svg",
  divider: "http://localhost:3845/assets/5179d5e43138aee71913de00fb5a8f0b7b113f8f.svg",
  blueLine: "http://localhost:3845/assets/316a2b45cd01176c4ad68425f14f739288b35bbc.svg",
  grayLine: "http://localhost:3845/assets/37060d531c628947a465b6fd77e989566cf1b2bc.svg"
};

export function StepIndicator() {
  return (
    <div className="bg-white flex gap-[16px] items-start p-0 relative shrink-0 w-full">
      
      {/* LEFT COLUMN: Icons & Lines */}
      <div className="flex flex-col gap-[6px] items-center relative shrink-0">
        
        {/* Check-circle */}
        <div className="overflow-clip relative shrink-0 w-[24px] h-[24px]">
          <div className="absolute inset-[8.33%]">
            <img alt="" className="absolute block inset-0 max-w-none w-full h-full object-contain" src={ICONS.checkCircle} />
          </div>
        </div>
        
        {/* Short Blue Line */}
        <div className="h-[12px] relative shrink-0 w-0">
          <div className="absolute inset-[-12.5%_-1.5px]">
            <img alt="" className="block max-w-none w-full h-full object-contain" src={ICONS.blueLine} />
          </div>
        </div>
        
        {/* Active Step (Receipt) */}
        <div className="bg-[#eaf1ff] flex items-center justify-center p-[12px] relative rounded-full shrink-0 w-[48px] h-[48px]">
          <div className="overflow-clip relative shrink-0 w-[24px] h-[24px]">
            <div className="absolute inset-[8.33%_12.5%_9.14%_12.5%]">
              <img alt="" className="absolute block inset-0 max-w-none w-full h-full object-contain" src={ICONS.receipt} />
            </div>
          </div>
        </div>
        
        {/* Long Divider (Blue -> Dot -> Gray) */}
        <div className="relative shrink-0 w-[19px] h-[64px]">
          <img alt="" className="absolute block inset-0 max-w-none w-full h-full object-contain" src={ICONS.divider} />
        </div>
        
        {/* Pencil-line */}
        <div className="overflow-clip relative shrink-0 w-[24px] h-[24px]">
          <div className="absolute inset-[8.33%]">
            <img alt="" className="absolute block inset-0 max-w-none w-full h-full object-contain" src={ICONS.pencil} />
          </div>
        </div>
        
        {/* Short Gray Line */}
        <div className="h-[12px] relative shrink-0 w-0">
          <div className="absolute inset-[-12.5%_-1.5px]">
            <img alt="" className="block max-w-none w-full h-full object-contain" src={ICONS.grayLine} />
          </div>
        </div>
        
        {/* Call */}
        <div className="overflow-clip relative shrink-0 w-[24px] h-[24px]">
          <div className="absolute inset-[12.5%]">
            <div className="absolute inset-[-5.56%]">
              <img alt="" className="block max-w-none w-full h-full object-contain" src={ICONS.call} />
            </div>
          </div>
        </div>
        
      </div>

      {/* RIGHT COLUMN: Content Blocks */}
      <div className="flex flex-1 flex-col gap-[24px] items-start justify-center min-w-0 relative shrink-0">
        
        {/* Content 1 */}
        <div className="flex items-center py-[2px] relative shrink-0 w-full h-[24px]">
          <div className="flex flex-1 flex-col justify-center leading-none min-w-0 relative">
            <p className="font-medium text-[#34404b] text-[14px] leading-[20px]">Nhận SIM</p>
          </div>
        </div>
        
        {/* Content 2 (Active Block) */}
        <div className="flex flex-col gap-[12px] items-start relative shrink-0 w-full h-[100px]">
          <div className="flex flex-col gap-[4px] items-start leading-none relative shrink-0 w-full">
            <div className="flex flex-col justify-center relative shrink-0 w-full">
              <p className="font-bold text-[#34404b] text-[16px] leading-[24px]">Xác thực giấy tờ tuỳ thân</p>
            </div>
            <div className="flex flex-col justify-center relative shrink-0 w-full">
              <p className="font-normal text-[#717981] text-[14px] leading-[20px]">Chụp ảnh giấy tờ tùy thân, ảnh chân dung</p>
            </div>
          </div>
          <div className="bg-[#3079ff] flex gap-[4px] items-center justify-center px-[16px] py-[10px] relative rounded-full shrink-0 w-full">
            <p className="font-bold leading-[20px] relative shrink-0 text-white text-[14px] whitespace-nowrap">
              Thực hiện ngay
            </p>
          </div>
        </div>
        
        {/* Content 3 */}
        <div className="flex items-center py-[2px] relative shrink-0 w-full h-[24px]">
          <div className="flex flex-1 flex-col justify-center leading-none min-w-0 relative">
            <p className="font-medium text-[#34404b] text-[14px] leading-[20px]">Ký hợp đồng</p>
          </div>
        </div>
        
        {/* Content 4 */}
        <div className="flex items-center py-[2px] relative shrink-0 w-full h-[24px]">
          <div className="flex flex-1 flex-col justify-center leading-none min-w-0 relative">
            <p className="font-medium text-[#34404b] text-[14px] leading-[20px]">Gọi 900 để hoàn tất kích hoạt</p>
          </div>
        </div>
        
      </div>
    </div>
  );
}
