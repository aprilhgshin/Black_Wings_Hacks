import React from 'react';
import { Button } from '../../globalStyles';
import { AiFillThunderbolt } from 'react-icons/ai';
import { GiCrystalBars } from 'react-icons/gi';
import { GiCutDiamond, GiRock } from 'react-icons/gi';
import { GiFloatingCrystal } from 'react-icons/gi';
import { IconContext } from 'react-icons/lib';
import {
  PricingSection,
  PricingWrapper,
  PricingHeading,
  PricingContainer,
  PricingCard,
  PricingCardInfo,
  PricingCardIcon,
  PricingCardPlan,
  PricingCardCost,
  PricingCardLength,
  PricingCardFeatures,
  PricingCardFeature
} from './Pricing.elements';

function Pricing() {
  return (
    <IconContext.Provider value={{ color: '#a9b3c1', size: 64 }}>
      <PricingSection>
        <PricingWrapper>
          <PricingHeading>The Facts of The Matter</PricingHeading>
          <PricingContainer>
            <PricingCard to='/sign-up'>
              <PricingCardInfo>
                <PricingCardIcon>
                  <GiRock />
                </PricingCardIcon>
                <PricingCardPlan>White Women Make</PricingCardPlan>
                <PricingCardCost>$0.98</PricingCardCost>
                <PricingCardLength>per every $1 White men make</PricingCardLength>
                <PricingCardFeatures>
                  <PricingCardFeature>Yearly Loss</PricingCardFeature>
                  <PricingCardFeature>-$10,000</PricingCardFeature>
                  {/* <PricingCardFeature>Retargeting analytics</PricingCardFeature> */}
                </PricingCardFeatures>
                <Button primary>Start Earning More</Button>
              </PricingCardInfo>
            </PricingCard>
            <PricingCard to='/sign-up'>
              <PricingCardInfo>
                <PricingCardIcon>
                  <GiCrystalBars />
                </PricingCardIcon>
                <PricingCardPlan>Black Women Make</PricingCardPlan>
                <PricingCardCost>$0.69</PricingCardCost>
                <PricingCardLength>per every $1 White men make</PricingCardLength>
                <PricingCardFeatures>
                  <PricingCardFeature>Yearly Loss</PricingCardFeature>
                  <PricingCardFeature>-$16,900</PricingCardFeature>
                  {/* <PricingCardFeature>Lead Gen Analytics</PricingCardFeature> */}
                </PricingCardFeatures>
                <Button primary>Start Earning More</Button>
              </PricingCardInfo>
            </PricingCard>
            <PricingCard to='/sign-up'>
              <PricingCardInfo>
                <PricingCardIcon>
                  <GiCutDiamond />
                </PricingCardIcon>
                <PricingCardPlan>Asian Men Make</PricingCardPlan>
                <PricingCardCost>117%</PricingCardCost>
                <PricingCardLength>more than White men</PricingCardLength>
                <PricingCardFeatures>
                  <PricingCardFeature>Yearly Gain</PricingCardFeature>
                  <PricingCardFeature>+20,900</PricingCardFeature>
                  {/* <PricingCardFeature>24/7 Support</PricingCardFeature> */}
                </PricingCardFeatures>
                <Button primary>Start Earning More</Button>
              </PricingCardInfo>
            </PricingCard>
          </PricingContainer>
        </PricingWrapper>
      </PricingSection>
    </IconContext.Provider>
  );
}
export default Pricing;
