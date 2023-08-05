//
// This file auto-generated with generate-wrappers.js
//

var _ = require('underscore');
var Promise = require('bluebird');
var THREE = require('three');
var widgets = require('@jupyter-widgets/base');
var dataserializers = require('jupyter-dataserializers');
var serializers = require('../_base/serializers');

var LightModel = require('./Light.autogen.js').LightModel;


class RectAreaLightModel extends LightModel {

    defaults() {
        return _.extend(LightModel.prototype.defaults.call(this), {

            width: 10,
            height: 10,
            type: "RectAreaLight",

        });
    }

    constructThreeObject() {

        var result = new THREE.RectAreaLight(
            this.convertColorModelToThree(this.get('color'), 'color'),
            this.convertFloatModelToThree(this.get('intensity'), 'intensity'),
            this.convertFloatModelToThree(this.get('width'), 'width'),
            this.convertFloatModelToThree(this.get('height'), 'height')
        );
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        LightModel.prototype.createPropertiesArrays.call(this);

        this.props_created_by_three['type'] = true;
        this.props_created_by_three['matrixWorldNeedsUpdate'] = true;

        this.property_converters['width'] = 'convertFloat';
        this.property_converters['height'] = 'convertFloat';
        this.property_converters['type'] = null;


    }
}

RectAreaLightModel.model_name = 'RectAreaLightModel';
RectAreaLightModel.serializers = {
    ...LightModel.serializers,
};

module.exports = {
    RectAreaLightModel: RectAreaLightModel,
};
