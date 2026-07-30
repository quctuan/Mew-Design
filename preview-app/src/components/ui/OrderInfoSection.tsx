import React from 'react';

const ASSETS = {
  atm: "http://localhost:3845/assets/5356ef4b32c7fb6c26decb721df2a778c661bcee.svg",
  eSim: "http://localhost:3845/assets/fb0b575e4ac8a353c0c22db245f9065397d72b7e.svg",
  dot: "http://localhost:3845/assets/91603899360c108d01bc969042d4b44d3bacce3d.svg",
  qrCode: "http://localhost:3845/assets/dd8bf18fafcf90bb25aecb4cf9f79996d473c895.svg",
  chevronRight: "http://localhost:3845/assets/c7cd6fc00bf5a7f57dafc422046cb3433dc93588.svg",
  copy: "http://localhost:3845/assets/e341e281aefe7d0690ceab1931341117f0d18c66.svg",
  chevronDown: "http://localhost:3845/assets/8b5cd1cdfd6cb6a3656e13f688405b23696bb0a8.svg",
  vnptLogo: "http://localhost:3845/assets/5618d1c3af22addede761d413eea50c3ea7551eb.svg",
  phone: "http://localhost:3845/assets/7d83303277361f33f611416b81878c2c0a9d3670.svg"
};

function IconPaymentMethod() {
  return (
    <div className="h-[20px] relative w-[29px] shrink-0">
      <div className="absolute bg-white border border-[#d9e1e2] border-solid inset-0 rounded-[3px]" />
      <div className="absolute inset-[31.39%_13.79%]">
        <img alt="" className="absolute block inset-0 max-w-none w-full h-full object-contain" src={ASSETS.atm} />
      </div>
    </div>
  );
}

export function OrderInfoCard() {
  return (
    <div className="bg-white border border-[#e0e0e0] border-solid flex flex-col gap-[12px] items-start pb-[8px] pt-[16px] px-[16px] rounded-[16px] w-full">
      {/* Header */}
      <div className="flex gap-[16px] items-center px-0 py-0 w-full shrink-0">
        <p className="flex-1 font-bold leading-[24px] text-[#34404b] text-[16px]">
          Thông tin đơn hàng
        </p>
      </div>

      {/* Content */}
      <div className="flex flex-col gap-[12px] items-start w-full shrink-0">
        <div className="flex flex-col gap-[16px] items-center w-full shrink-0">
          
          {/* SIM info block */}
          <div className="flex gap-[12px] items-center overflow-clip w-full shrink-0">
            {/* Icon */}
            <div className="bg-white border border-[#e0e0e0] border-solid flex items-center justify-center p-[5px] rounded-[32px] shrink-0 w-[48px] h-[48px]">
              <div className="bg-white overflow-clip relative shrink-0 w-[32px] h-[32px]">
                <div className="absolute inset-[-3.27%_-4.16%_-3.31%_-4.22%]">
                  <img alt="" className="block max-w-none w-full h-full object-contain" src={ASSETS.eSim} />
                </div>
              </div>
            </div>
            
            {/* Text details */}
            <div className="flex flex-col gap-[2px] h-[46px] items-start flex-1 min-w-0">
              <p className="font-medium leading-[24px] text-[#34404b] text-[16px]">0842 316 555</p>
              <div className="flex gap-[4px] items-center shrink-0">
                <p className="font-normal leading-[20px] text-[#34404b] text-[14px] whitespace-nowrap">Thuê bao trả trước</p>
                <div className="relative shrink-0 w-[4px] h-[4px]">
                  <div className="absolute left-[0.5px] top-[0.5px] w-[3px] h-[3px]">
                    <img alt="" className="absolute block inset-0 max-w-none w-full h-full object-contain" src={ASSETS.dot} />
                  </div>
                </div>
                <p className="font-normal leading-[20px] text-[#34404b] text-[14px] whitespace-nowrap">eSIM</p>
              </div>
            </div>
          </div>

          {/* Button Xem thông tin eSIM */}
          <button className="bg-white border border-[#3079ff] border-solid flex gap-[4px] items-center justify-center px-[16px] py-[10px] rounded-full shrink-0 w-full">
            <div className="overflow-clip relative shrink-0 w-[20px] h-[20px]">
              <div className="absolute inset-[8.33%]">
                <img alt="" className="absolute block inset-0 max-w-none w-full h-full object-contain" src={ASSETS.qrCode} />
              </div>
            </div>
            <span className="font-bold leading-[20px] text-[#3079ff] text-[14px] whitespace-nowrap">
              Xem thông tin eSIM
            </span>
          </button>
        </div>

        {/* Details list */}
        <div className="flex flex-col items-center w-full shrink-0">
          
          {/* Cell 1: Tổng thanh toán */}
          <div className="flex gap-[24px] items-center py-[8px] w-full shrink-0">
            <p className="flex-1 font-normal leading-[20px] text-[#717981] text-[14px]">Tổng thanh toán</p>
            <div className="flex flex-1 gap-[4px] items-center justify-end min-w-0">
              <p className="font-bold leading-[20px] text-[#34404b] text-[14px] truncate text-right">179.500đ</p>
              <div className="overflow-clip relative shrink-0 w-[20px] h-[20px]">
                <div className="absolute inset-[8.33%]">
                  <img alt="" className="absolute block inset-0 max-w-none w-full h-full object-contain" src={ASSETS.chevronRight} />
                </div>
              </div>
            </div>
          </div>

          {/* Cell 2: Phương thức thanh toán */}
          <div className="flex gap-[24px] items-center py-[8px] w-full shrink-0">
            <p className="flex-1 font-normal leading-[20px] text-[#717981] text-[14px]">Phương thức thanh toán</p>
            <div className="flex flex-1 gap-[4px] items-center justify-end min-w-0">
              <IconPaymentMethod />
              <p className="font-medium leading-[20px] text-[#34404b] text-[14px] truncate">*0384</p>
            </div>
          </div>

          {/* Cell 3: Mã đơn hàng */}
          <div className="flex gap-[24px] items-start py-[8px] w-full shrink-0">
            <p className="flex-1 font-normal leading-[20px] text-[#717981] text-[14px]">Mã đơn hàng</p>
            <div className="flex gap-[4px] items-center shrink-0 justify-end">
              <p className="font-medium leading-[20px] text-[#34404b] text-[14px] whitespace-nowrap">2512017U3P9J1G</p>
              <div className="overflow-clip relative shrink-0 w-[20px] h-[20px]">
                <div className="absolute inset-[8.33%]">
                  <img alt="" className="absolute block inset-0 max-w-none w-full h-full object-contain" src={ASSETS.copy} />
                </div>
              </div>
            </div>
          </div>

          {/* Button Xem chi tiết */}
          <button className="flex gap-[4px] items-center justify-center p-[8px] rounded-full shrink-0 mt-[4px]">
            <span className="font-bold leading-[20px] text-[#34404b] text-[14px] whitespace-nowrap">
              Xem chi tiết
            </span>
            <div className="overflow-clip relative shrink-0 w-[16px] h-[16px]">
              <div className="absolute inset-[8.33%]">
                <img alt="" className="absolute block inset-0 max-w-none w-full h-full object-contain" src={ASSETS.chevronDown} />
              </div>
            </div>
          </button>
        </div>

      </div>
    </div>
  );
}

export function SupportCard() {
  return (
    <div className="bg-white border border-[#e0e0e0] border-solid flex flex-col items-center overflow-clip p-[16px] rounded-[16px] w-full shrink-0">
      <div className="flex flex-col gap-[8px] items-start w-full shrink-0">
        <div className="flex gap-[16px] items-center w-full shrink-0">
          <p className="flex-1 font-bold leading-[24px] text-[#34404b] text-[16px]">
            Tổng đài hỗ trợ
          </p>
        </div>
        <div className="flex flex-col gap-[12px] items-start w-full shrink-0">
          <p className="font-normal leading-[20px] text-[#34404b] text-[14px] w-full">
            Để được hỗ trợ dịch vụ, bạn vui lòng liên hệ:
          </p>
          <div className="flex gap-[8px] items-center w-full shrink-0">
            {/* Logo VinaPhone */}
            <div className="bg-[#3079ff] flex gap-[10px] items-center p-[10px] rounded-full shrink-0">
              <div className="overflow-clip relative shrink-0 w-[20px] h-[20px]">
                <div className="absolute inset-[10%]">
                  <img alt="" className="absolute block inset-0 max-w-none w-full h-full object-contain" src={ASSETS.vnptLogo} />
                </div>
              </div>
            </div>
            
            {/* Texts */}
            <div className="flex flex-col flex-1 items-start min-w-0">
              <p className="font-normal leading-[16px] text-[#717981] text-[12px] w-full">Tổng đài VinaPhone</p>
              <div className="flex gap-[8px] items-center w-full shrink-0">
                <p className="font-bold leading-[24px] text-[#34404b] text-[16px] whitespace-nowrap">1800 1091</p>
              </div>
            </div>

            {/* Call button */}
            <button className="bg-white border border-[#3079ff] border-solid flex gap-[4px] items-center justify-center px-[12px] py-[12px] rounded-full shrink-0 w-[40px] h-[40px]">
              <div className="overflow-clip relative shrink-0 w-[20px] h-[20px]">
                <div className="absolute inset-[8.33%]">
                  <img alt="" className="absolute block inset-0 max-w-none w-full h-full object-contain" src={ASSETS.phone} />
                </div>
              </div>
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export function OrderInfoSection() {
  return (
    <div className="flex flex-col w-full">
      <OrderInfoCard />
      <SupportCard />
    </div>
  );
}
