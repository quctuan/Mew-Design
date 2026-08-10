import React from 'react';
import { StepIndicator } from './StepIndicator';

const ASSETS = {
  illustration: "http://localhost:3845/assets/5ce06f60181796d041d0245545ae569912c5994d.png"
};

export function OrderTrackingSection() {
  return (
    <div className="relative flex flex-col w-full shrink-0 pt-[68px]">
      
      {/* Background Yellow Banner (Absolute) */}
      <div className="absolute top-0 left-0 w-full bg-[#fff2d7] rounded-tl-[16px] rounded-tr-[16px] pt-[16px] pb-[48px] pl-[16px] pr-[64px] flex flex-col justify-start">
        <p className="font-medium text-[14px] leading-[20px] text-[#34404b]">
          Thời gian cần hoàn tất kích hoạt SIM:
          <br />
          Trước 14:30 - 04/12
        </p>
        
        {/* Illustration overlapping the banner */}
        <div className="absolute top-[-42px] right-0 w-[110px] h-[110px]">
          <div className="absolute top-0 right-[-6px] w-[118px] h-[110px]">
            <img 
              src={ASSETS.illustration} 
              alt="Illustration" 
              className="absolute w-[139.83%] h-full top-[6.26%] left-[-9.23%] max-w-none object-contain pointer-events-none" 
            />
          </div>
        </div>
      </div>

      {/* Foreground White Card (Relative) */}
      <div className="relative bg-white border border-[#e0e0e0] rounded-[16px] p-[16px] flex flex-col gap-[16px] w-full z-10 shadow-sm">
        <h2 className="text-[16px] font-bold text-[#34404b] leading-[24px]">
          Theo dõi đơn hàng
        </h2>
        <StepIndicator />
      </div>
    </div>
  );
}
